import requests
import time
import json
from video import Video
from functions import check_api_resp, get_video_id
from datetime import datetime


# Get video ID information
video_params = get_video_id()

# Loop settings
call_count = 0
view_last = 0
wait_time = 30
wait_time_failed = 30

# Main loop
while True:
    # Record count
    call_count += 1
    print(f"\nStarting API call No. {call_count}")

    # Call video static API and check response
    video_request_url = "https://api.bilibili.com/x/web-interface/view"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                      'like Gecko) Chrome/91.0.4472.101 Safari/537.36'
    }
    r = requests.get(video_request_url, params=video_params, headers=headers)
    video_static_info = r.json()
    if check_api_resp(r.status_code, video_static_info):
        time.sleep(wait_time_failed)
        continue

    # Call video dynamic API and check response
    video_request_url = "http://api.bilibili.com/x/web-interface/archive/stat"
    r = requests.get(video_request_url, params=video_params, headers=headers)
    video_dynamic_info = r.json()
    if check_api_resp(r.status_code, video_dynamic_info):
        time.sleep(wait_time_failed)
        continue

    # Process API response
    video = Video(video_static_info['data'], video_dynamic_info['data'])

    now = datetime.now()
    upload_time = datetime.fromtimestamp(video.pubdate)
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f'--Video Title: {video.title}')
    print(f'--Publish Time: {upload_time}')
    print(f'--Current Time: {current_time}')
    print(f'--Current Views: {video.view}')

    if call_count > 1:
        print(f'--View increase since last call: {video.view - view_last}')
    view_last = video.view

    # Store video information
    current_info = {
        'recorded_time': current_time,
        'static_info': video.generate_static_class(),
        'dynamic_info': video.generate_dynamic_class(),
    }

    with open(f'records/{video.bvid}_record.csv', 'a') as f:
        f.write(f'{json.dumps(current_info)},')

    # Wait for ** seconds
    print(f"Completed API call No. {call_count}")
    time.sleep(wait_time)



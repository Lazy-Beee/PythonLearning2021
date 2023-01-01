import requests


# Check API response, return True if error occurred
def check_api_resp(status_code, json):
    if status_code == 200:
        if json['code'] == 0:
            print(f"Video access is successful")
            return False
        else:
            print(f"Video access failed with\n\tcode: {json['code']}"
                  f"\tmessage: {json['message']}")
            return True
    else:
        print(f"API request failed with status code: {status_code}\tmessage: {json['message']}")
        return True


def get_video_id():
    while True:
        video_id = str(input("Enter video ID starting with AV/BV: "))
        if (video_id[:2]).lower() == 'av':
            video_params = f'aid={video_id[2:]}'
            break
        elif (video_id[:2]).lower() == 'bv':
            video_params = f'bvid={video_id[2:]}'
            break
        # Test case
        elif video_id == '':
            video_params = 'bvid=1ig411g7aX'
            break
        else:
            print("Can't interpret video ID")

    return video_params

def get_video_id_bv():
    while True:
        video_id = str(input("Enter video ID starting with AV/BV: "))
        if (video_id[:2]).lower() == 'av':
            video_params = video_id[2:]
            break
        elif (video_id[:2]).lower() == 'bv':
            video_params = video_id[2:]
            break
        # Test case
        elif video_id == '':
            video_params = '1ig411g7aX'
            break
        else:
            print("Can't interpret video ID")

    return video_params
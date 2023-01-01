import json
from operator import itemgetter
import requests

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

error_url, error_comment = 0, 0

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids:
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    progress = (submission_ids.index(submission_id) + 1) / len(
        submission_ids) * 100
    print(f"id: {submission_id}\tstatus: {r.status_code}\t\tprogress: "
          f"{'{:.3}'.format(progress)}%")
    response_dict = r.json()

    try:
        comments = response_dict['descendants']
    except KeyError:
        comments = -1
        print(f'---------------------WARNING----------------------\n'
              f'Error in extracting comment of article id {submission_id}'
              f'\n--------------------------------------------------')
        error_comment += 1

    try:
        submission_url = response_dict['url']
    except KeyError:
        submission_url = 'Not Available'
        print(f'-------------------WARNING--------------------\n'
              f'Error in extracting url of article id {submission_id}'
              f'\n----------------------------------------------')
        error_url += 1

    submission_dict = {
        'title': response_dict['title'],
        'hn_link': submission_url,
        'comments': comments
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

hn_news = {'article': []}
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

    hn_news['article'].append({
        'title': submission_dict['title'],
        'discussion link': submission_dict['hn_link'],
        'comments': submission_dict['comments'],
    })

with open('data/sorted_hn_news.json', 'w') as outfile:
    json.dump(hn_news, outfile, indent=4)

print(f'\nFailed to extract comment: {error_comment}')
print(f'Failed to extract url: {error_url}')
print(f'Failed to extract article:'
      f' {len(submission_ids) - len(submission_dicts)}')

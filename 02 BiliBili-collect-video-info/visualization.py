from plotly import offline
from operator import itemgetter
from functions import get_video_id_bv
import ast

bvid = get_video_id_bv()

with open(f'records/BV{bvid}_record.csv', 'r') as f:
    records = ast.literal_eval(f.read())

records = sorted(records, key=itemgetter('recorded_time'))
record_times, record_views = [], []
for info in records:
    record_times.append(info['recorded_time'])
    record_views.append(info['dynamic_info']['view'])
# Make visualization
data = [{
    'x': record_times,
    'y': record_views,
}]
my_layout = {
    'title': f'View of BV{bvid}, {records[0]["static_info"]["title"]}',
    'xaxis': {
        'title': 'Time',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'View',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename=f'records/View of BV{bvid}.html')
class Video:
    def __init__(self, video_static_data, video_dynamic_data):
        self.data1 = video_static_data
        self.data2 = video_dynamic_data

        self.bvid = self.data1['bvid']
        self.title = self.data1['title']
        self.pubdate = self.data1['pubdate']
        self.desc = self.data1['desc']
        self.duration = self.data1['duration']
        self.owner_mid = self.data1['owner']['mid']
        self.owner_name = self.data1['owner']['name']
        self.state = self.data1['state']

        if not self.data2['view'] == '--':
            self.view = self.data2['view']
        else:
            self.view = -1
        self.danmu = self.data2['danmaku']
        self.reply = self.data2['reply']
        self.favorite = self.data2['favorite']
        self.coin = self.data2['coin']
        self.share = self.data2['share']
        self.history_rank = self.data2['his_rank']
        self.like_rank = self.data2['like']

    def generate_static_class(self):
        video_static_info = {
            'bvid': self.bvid,
            'title': self.title,
            'pubdate': self.pubdate,
            'description': self.desc,
            'duration': self.duration,
            'owner_mid': self.owner_mid,
            'owner_name': self.owner_name,
            'state': self.state
        }
        return video_static_info

    def generate_dynamic_class(self):
        video_dynamic_info = {
            'view': self.view,
            'danmaku': self.danmu,
            'reply': self.reply,
            'favorite': self.favorite,
            'coin': self.coin,
            'share': self.share,
            'his_rank': self.history_rank,
            'like': self.like_rank
        }
        return video_dynamic_info


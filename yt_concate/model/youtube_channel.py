import os
from yt_concate.user_input import CAPTIONS_DIR, VIDEOS_DIR


class YoutubeChannel:
    def __init__(self, url):
        self.url = url
        self.id = self.get_video_id_from_url()
        self.caption_file_path = self.get_caption_file_path()
        self.video_file_path = self.get_video_file_path()
        # self.caption

    @staticmethod
    def get_video_id_from_url(url):  # get video id from url
        return url.split('watch?v=')[1]

    def get_caption_file_path(self):  # get caption file path
        return os.path.join(CAPTIONS_DIR, self.id + '.txt')

    def get_video_file_path(self):  # get caption file path
        return os.path.join(VIDEOS_DIR, self.id + '.txt')
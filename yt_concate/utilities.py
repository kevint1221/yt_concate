import os

from yt_concate.user_input import CAPTIONS_DIR, VIDEOS_DIR, DOWNLOADS_DIR

class Utilities:
    def __init__(self):
        pass

    @staticmethod
    def create_dir():  # create dir path for video and caption folder
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)

    def caption_file_exists(self, youtubechannel):  # get video id as caption file name
        path = youtubechannel.get_caption_file_path()
        return os.path.exists(path) and os.path.getsize(path) > 0

    def get_video_list_file_path(self, channel_id):  # get video list file path
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_file_exits(self, channel_id):  # check if channel id already existed
        path = self.get_video_list_file_path(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0


from pytube import YouTube

from .step import Step
from yt_concate.user_input import VIDEOS_DIR


class DownloadVideo(Step):
    def process(self, data, inputs, utils):
        for found in data:
            url = found.youtubechannel.url
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=)




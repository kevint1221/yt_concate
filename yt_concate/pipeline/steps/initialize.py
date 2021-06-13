from .step import Step
from yt_concate.model.youtube_channel import YoutubeChannel


class Initialize(Step):
    def process(self, data, inputs, utils):
        return [YoutubeChannel(url) for url in data]  # get very url from data and pass in Youtubechannel


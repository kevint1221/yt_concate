from .step import Step
from yt_concate.model.found import Found


class Search(Step):
    def process(self, data, inputs, utils):
        search_word = inputs['search_word']
        found = []
        for youtubechannel in data:
            captions = youtubechannel.captions
            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    f = Found(youtubechannel, caption, time)
                    found.append(f)
        return found

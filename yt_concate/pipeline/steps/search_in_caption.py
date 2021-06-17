from .step import Step
from yt_concate.model.found import Found


class Search(Step):
    def process(self, data, inputs, utils):
        search_word = inputs['search_word']
        found = []
        for youtubechannel in data:
            captions = youtubechannel.captions
            if not captions:  # we are checking every youtube channel no matter we download  caption or not, so need to check this
                continue
            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    f = Found(youtubechannel, caption, time)
                    found.append(f)
        print("executing found")
        for i in found:
            print(i.caption)
        return found

from .step import Step


class Search(Step):
    def process(self, data, inputs, utils):
        search_word = inputs['search_word']
        found = []
        for youtubechannel in data:
            captions = youtubechannel.captions
            for caption in captions:
                if search_word in caption:
                    found.append(youtubechannel)

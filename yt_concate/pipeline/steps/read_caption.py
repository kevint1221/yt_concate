import os
import pprint
from yt_concate.utilities import CAPTIONS_DIR
from .step import Step


# We are going to read each file, if find timeline or caption, stores they in the library
# time as a key, caption is the value
class ReadCaption(Step):
    def process(self, data, inputs, utils):

        for youtubechannel in data:
            #  if caption doesn't exist in the folder, do nothing
            if not utils.caption_file_exists(youtubechannel):
                continue
            captions = {}
            with open(youtubechannel.caption_file_path, 'r') as f:
                # store time and caption in dictionary for later use
                time_line = True
                time = None
                caption = None
                for line in f:
                    if '-->' in line:  # found line with time
                        time_line = True  # found time line, next line must be caption
                        time = line.strip()
                        continue
                    if time_line:  # if time_line is true
                        caption = line.strip()
                        captions[caption] = time  # we use caption as key so we can loop keyword to get time easier
                        time_line = False
            youtubechannel.captions = captions   # only changes here
        return data


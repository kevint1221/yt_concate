import os
from yt_concate.utilities import CAPTIONS_DIR
from .step import Step


# We are going to read each file, if find timeline or caption, stores they in the library
# time as a key, caption is the value
class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}  # data dictionary contain caption dictionary for each video
        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {}  # dictionary for all caption in this file
            with open(caption_file, 'r') as f:
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
            data[caption_file] = captions  # store dictionary of each video into data
        print(data)
        return data


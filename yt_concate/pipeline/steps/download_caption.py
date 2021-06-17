import os

from pytube import YouTube

from .step import Step
from .step import StepException


class DownloadCaption(Step):
    def process(self, data, inputs, utils):
        print(data)
        #data2 = ["https://youtu.be/1QHJksTrk8s"]
        for youtube_channel in data:

            # No caption available handling, caption doesn't always available or auto-generated
            if utils.caption_file_exists(youtube_channel):
                print('caption existed')
                continue

            print("generating caption for", youtube_channel.url)
            # error unknown download error handling
            try:
                source = YouTube(youtube_channel.url)

            except KeyError as k:
                print('encountered ', k, 'that this caption cannot be downloaded')

            en_caption_convert_to_str = ""

            print(source.captions)
            language_code = find_caption_code(source)

            if len(language_code) != 0:
                en_caption = source.captions.get_by_language_code(language_code)
                en_caption_convert_to_str = en_caption.generate_srt_captions()

            # if en_caption_convert_to_str never get generated caption
            if len(en_caption_convert_to_str) != 0:
                print("writing to file now")
                text_file = open(youtube_channel.caption_file_path, 'w', encoding='utf-8')
                text_file.write(en_caption_convert_to_str)
                text_file.close()
                print()
        return data

def find_caption_code(source):
    english = False
    auto_english = False

    for caption in source.captions:
        if caption.code == "en":
            english = True
        if caption.code == "a.en":
            auto_english = True
    if english:
        language_code = "en"
    elif auto_english:
        language_code = "a.en"
    else:
        language_code = ""
    return language_code



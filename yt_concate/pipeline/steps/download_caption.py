import os

from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

from .step import Step
from .step import StepException


class DownloadCaption(Step):
    def process(self, data, inputs, utils):
        #en_caption_convert_to_srt = None
        # print()
        # print('https://www.youtube.com/watch?v=WQ6DpK780gM')
        # # transcript_list = YouTubeTranscriptApi.list_transcripts(x[1])
        # # transcript_list = YouTubeTranscriptApi.list_transcripts('nkFMDApJ8iA')
        # # transcript = transcript_list.find_transcript(['en'])
        # # source = YouTube('https://www.youtube.com/watch?v=WQ6DpK780gM')
        # #source = YouTube('https://www.youtube.com/watch?v=WQ6DpK780gM')
        # #source = YouTube('https://www.youtube.com/watch?v=NFHDHcs4BvQ')
        # source = YouTube('https://www.youtube.com/watch?v=nkFMDApJ8iA')
        # print('Captions Available: ', source.captions)

        for url in data:
            print(url)
            # No caption available handling, caption doesn't always available or auto-generated
            if utils.caption_file_exists(url):
                print('caption existed')
                continue

            try:
                source = YouTube(url)
            except KeyError as k:
                print('encountered ', k, 'that this caption cannot be downloaded')

            en_caption_convert_to_str = None

            try:
                en_caption = source.captions.get_by_language_code('en')
                en_caption_convert_to_str = en_caption.generate_srt_captions()
            except AttributeError:
                try:
                    en_caption = source.captions.get_by_language_code('a.en')  # auto-genereated by youtube
                    en_caption_convert_to_str = en_caption.generate_srt_captions()
                except AttributeError:
                    print("no caption for this video")
                    print()
                    continue
            ## print(en_caption_convert_to_str)

            text_file = open(utils.get_caption_file_path(url) + '.txt', 'w', encoding='utf-8')
            text_file.write(en_caption_convert_to_str)
            text_file.close()
            print()


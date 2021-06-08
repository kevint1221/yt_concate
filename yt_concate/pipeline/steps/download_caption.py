from pytube import YouTube

from .step import Step
from .step import StepException


class DownloadCaption(Step):
    def process(self, data, inputs):
        #en_caption_convert_to_srt = None
        #for url in data:
        #print(url)
        source = YouTube('https://www.youtube.com/watch?v=sW9npZVpiMI')
        en_caption = source.captions.get_by_language_code('en')
        en_caption_convert_to_srt = (en_caption.generate_srt_captions())
        print(en_caption_convert_to_srt)
        return en_caption_convert_to_srt
        """
        for url in data:
            source = YouTube(url)
            en_caption = source.captions.get_by_language_code('en')
            en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            #print(en_caption_convert_to_srt)
            #save the caption to a file named Output.txt
            text_file = open("Output.txt", "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
            break
        """
        #return en_caption_convert_to_srt


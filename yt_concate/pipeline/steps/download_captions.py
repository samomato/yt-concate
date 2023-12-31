import time
from pytube import YouTube
from yt_concate.utils import Utils
from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        # download the package by:  pip install pytube
        start = time.time()
        for yt in data:
            print('downloading caption for', yt.id)
            if Utils.caption_file_exists(yt):
                print('found existing caption file')
                continue
            try:
                source = YouTube(yt.url)
                caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (caption.generate_srt_captions())
            except (KeyError, AttributeError):
                print('KeyError when downloading for', yt.url)
                continue

            text_file = open(utils.get_caption_filepath(yt.url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
            # break
        end = time.time()
        print('took', end - start, 'seconds')

        return data
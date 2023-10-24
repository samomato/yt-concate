import os

from pprint import pprint
from .step import Step
from yt_concate.settings import CAPTIONS_DIR

class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}
        for file in os.listdir(CAPTIONS_DIR):
            captions = {}
            with open(os.path.join(CAPTIONS_DIR, file), 'r') as f:
                time = None
                caption = None
                time_line = False
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True
                        time = line
                        continue
                    elif time_line:
                        caption = line
                        captions[caption] = time
                        time_line = False
            data[file] = captions

        pprint(data)
        return data



from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.posflight import Posflight
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipline import Pipeline
from .utils import Utils

CHANNEL_ID = 'UCSri6c58uWro3kLTlcuFlVA'

def main():
    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        ReadCaption,
        Posflight(),
         ]
# 這裡上下都用多行式的寫法
    inputs = {
        'channel_id': CHANNEL_ID
    }
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    # main check, 上述意思是：如果執行的這個檔案是程式的進入點
    # 意思是就算是檔名不是main，只要這個程式是進入點，py就會自動把__name__這個屬性存成__main__
    main()
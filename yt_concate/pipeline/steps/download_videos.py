from .step import Step

from pytube import YouTube

from yt_concate.settings import VIDEOS_DIR
class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        print('videos to download:', len(yt_set))
        # set()可以把清單中重複的元素淘汰掉

        for yt in yt_set:
            url = yt.url
            print('downloading', url)
            if utils.video_file_exists(yt):
                print(f'found existing video file for {url}, skipping')
                continue
            print('downloading', url)
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)

        return data
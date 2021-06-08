"""
This Project will seize all youtube video from channel, download each video subtitle, download video, and then edit video

1. needs a official API key to get data from youtube
    - code source: https://stackoverflow.com/questions/15512239/python-get-all-youtube-video-urls-of-a-channel
    - There is usually a quotas which limit how many time you can access youtube to get data
    - API key: AIzaSyA_hVoPkhHJpczjjRVG74XurSs9H8F1s5w
        - API shouldn't be push to github for public uses
2. get channel id: https://socialnewsify.com/get-channel-id-by-username-youtube/
"""

from yt_concate.pipeline.steps.get_url import GetVideoList
from yt_concate.pipeline.steps.download_caption import DownloadCaption
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.user_input import inputs


# This project is using pipeline design pattern
# Each task is a process in the steps
# We execute each step in a pipeline
def main():
    steps = [
        GetVideoList(),
        DownloadCaption(),
    ]
    p = Pipeline(steps)
    p.run(inputs)


# make sure we are not execute anything else except main function
if __name__ == '__main__':
    main()

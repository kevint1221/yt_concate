"""
This Project will seize all youtube video from channel, download each video subtitle, download video, and then edit video
Each function is organized using Pipeline Design Pattern.

##########################Procedure:
1. needs a official API key to get data from youtube
    - code source: https://stackoverflow.com/questions/15512239/python-get-all-youtube-video-urls-of-a-channel
    - There is usually a quotas which limit how many time you can access youtube to get data
    - API key: AIzaSyA_hVoPkhHJpczjjRVG74XurSs9H8F1s5w
        - API shouldn't be push to github for public uses
    - get channel id: https://socialnewsify.com/get-channel-id-by-username-youtube/
    - KNOWN ERROR: 403 forbidden happens when reached quota limits
2. Download each video caption using pytube library
3.

"""

from yt_concate.pipeline.steps.get_url import GetVideoList
from yt_concate.pipeline.steps.download_caption import DownloadCaption
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.setup import Setup
from yt_concate.pipeline.steps.cleanup import Cleanup
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.user_input import inputs
from yt_concate.utilities import Utilities

# This project is using pipeline design pattern
# Each task is a process in the steps
# We execute each step in a pipeline


def main():
    steps = [
        Setup(),
        GetVideoList(),
        DownloadCaption(),
        #ReadCaption()

        #Cleanup()
    ]
    utils = Utilities()
    p = Pipeline(steps)
    p.run(inputs, utils)


# make sure we are not execute anything else except main function
if __name__ == '__main__':
    main()

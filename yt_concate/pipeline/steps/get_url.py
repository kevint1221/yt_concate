"""
This is the first step:
getting all video urls from youtube channel
"""

import urllib.request
import json

from yt_concate.pipeline.steps.step import Step


class GetVideoList(Step):
    def process(self, data, inputs, utils):
        channel_id = inputs['channel_id']
        api_key = inputs['api_key']

        base_video_url = 'https://www.youtube.com/watch?v='
        # ask what channel is needed
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
        # maximum search for each page set to 25 to prevent quotas limit
        first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

        video_links = []
        url = first_url
        while True:
            # connect to the video url
            inp = urllib.request.urlopen(url)
            # response
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']

                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                # if at the last page then error will show up here and stop the while loop
                # keyError will arise here
                break
        print(len(video_links))  #### this can be remove later
        print(video_links)
        return video_links


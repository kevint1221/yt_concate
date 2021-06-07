"""
This Project will seize all youtube video from channel, download each video subtitle, download video, and then edit video

1. needs a official API key to get data from youtube
    - code source: https://stackoverflow.com/questions/15512239/python-get-all-youtube-video-urls-of-a-channel
    - There is usually a quotas which limit how many time you can access youtube to get data
    - API key: AIzaSyA_hVoPkhHJpczjjRVG74XurSs9H8F1s5w
        - API shouldn't be push to github for public uses
2. get channel id: https://socialnewsify.com/get-channel-id-by-username-youtube/
"""

import urllib.request
import json
import api_key

# takes linus tec as example
CHANNEL_ID = 'UCXuqSBlHAE6Xw-yeJA0Tunw'


def get_all_video_in_channel(channel_id):
    api = api_key.key
    base_video_url = 'https://www.youtube.com/watch?v='
    # ask what channel is needed
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
    # maximum search for each page set to 25 to prevent quotas limit
    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api, channel_id)

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
    return video_links


video_list = get_all_video_in_channel(CHANNEL_ID)
print(len(video_list))
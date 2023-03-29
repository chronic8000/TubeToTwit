import os
import time
import random
import requests
import googleapiclient.discovery
import tweepy

# Set up Twitter API keys and access tokens
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Set up YouTube API client
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "YOUR_DEVELOPER_KEY"
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)

# Fetch all videos from your channel
videos = []
next_page_token = None
while True:
    request = youtube.search().list(
        part="snippet",
        channelId="YOUR_CHANNEL_ID",
        maxResults=50,
        order="date",
        pageToken=next_page_token,
        type="video"
    )
    response = request.execute()
    videos += response['items']
    next_page_token = response.get('nextPageToken')
    if next_page_token is None:
        break

# Choose a random video from the list
video = random.choice(videos)['snippet']

# Extract video title and thumbnail URL
title = video['title']
thumbnail_url = video['thumbnails']['high']['url']

# Download thumbnail image and save to a local file
response = requests.get(thumbnail_url)
with open('thumbnail.jpg', 'wb') as f:
    f.write(response.content)

# Post title and thumbnail to Twitter
media = api.media_upload('thumbnail.jpg')
tweet = f"{title} {media.media_id_string}"
api.update_status(status=tweet)

# Remove the local file
os.remove('thumbnail.jpg')

# Wait for three hours before running the script again
time.sleep(3 * 60 * 60)

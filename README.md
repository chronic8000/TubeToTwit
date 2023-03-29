# TubeToTwit
Post one of your YouTube videos from your channel to Twitter via python

Replace the YOUR_CONSUMER_KEY, YOUR_CONSUMER_SECRET, YOUR_ACCESS_TOKEN, YOUR_ACCESS_TOKEN_SECRET, YOUR_DEVELOPER_KEY, and YOUR_CHANNEL_ID placeholders with your actual API keys and channel ID, respectively.

This script uses the youtube.search() method to retrieve all videos from your channel, sorts them by date in descending order, and stores them in a list. It then chooses a random video from the list, extracts its title and thumbnail URL, and posts them to Twitter using the update_status method of the tweepy API. Finally, it waits for three hours before running the script again using the time.sleep function.

import tweepy


class StreamListener(tweepy.StreamingClient):

    def __init__(self, api, bearer_token, **kwargs):
        super().__init__(bearer_token, **kwargs)
        self.api = api
        #self.me = api.me()

    # the function containing the logic on what to do for each tweet
    def on_status(self, tweet):
        # We only want the bot to retweet original tweets, not replies.
        # We also don't want the bot to retweet itself
        if tweet.in_reply_to_status_id is not None or \
                tweet.use.id == self.me.id:
            return  # If we haven't retweeted this tweet yet, retweet it
        if not tweet.retweeted:
            try:
                tweet.retweet()
                print("Tweet retweeted successfully")
            except Exception as e:
                print(e)  # If we haven't favorited this tweet yet, favorite it
        if not tweet.favorited:
            try:
                tweet.favorite()
                print("Tweet favorited successfully")
            except Exception as e:
                print(e)

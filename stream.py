import tweepy
from tweepy import StreamRule

import config

# streaming_client = tweepy.StreamingClient(config.BEARER_TOKEN)
#
# streaming_client.add_rules(tweepy.StreamRule("Tweepy"))
client = tweepy.Client(consumer_key=config.API_KEY,
                       consumer_secret=config.API_SECRET,
                       access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET)


class TweetPrinterV2(tweepy.StreamingClient):

    def on_tweet(self, tweet):
        print(f"{tweet.id} ({tweet.author_id}): {tweet.text}")
        print("-" * 50)

        response = client.retweet(tweet.id)
        print(response)


printer = TweetPrinterV2(config.BEARER_TOKEN)
#
# # add new rules
rule = StreamRule(value="")
printer.add_rules(rule)



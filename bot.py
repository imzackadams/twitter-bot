import tweepy
from tweepy import StreamingClient, StreamRule
import config

bearer_token = config.BEARER_TOKEN

client = tweepy.Client(consumer_key=config.API_KEY,
                       consumer_secret=config.API_SECRET,
                       access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET)


class TweetPrinterV2(tweepy.StreamingClient):

    def on_tweet(self, tweet):
        print(f"{tweet.id} {tweet.created_at} ({tweet.author_id}): {tweet.text}")
        print("-" * 50)
        response = client.retweet(tweet.id)
        print(response)


printer = TweetPrinterV2(bearer_token)

rule_ids = []
result = printer.get_rules()
for rule in result.data:
    print(f"rule marked to delete: {rule.id} - {rule.value}")
    rule_ids.append(rule.id)

if len(rule_ids) > 0:
    printer.delete_rules(rule_ids)
    printer = TweetPrinterV2(bearer_token)
else:
    print("no rules to delete")

# add new rules
rule = StreamRule(value="amber heard")
printer.add_rules(rule)

printer.filter(expansions="author_id", tweet_fields="created_at")

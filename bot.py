import tweepy
from tweepy import StreamRule
import time
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

client = tweepy.Client(consumer_key=os.environ.get("API_KEY"),
                       consumer_secret=os.environ.get("API_KEY_SECRET"),
                       access_token=os.environ.get("ACCESS_TOKEN"),
                       access_token_secret=os.environ.get("ACCESS_TOKEN_SECRET"))


class TweetPrinterV2(tweepy.StreamingClient):

    def on_tweet(self, tweet):
        print(f"{tweet.id} {tweet.created_at} ({tweet.author_id}): {tweet.text}")
        print("-" * 50)
        time.sleep(30)

        try:
            response = client.retweet(tweet.id)
            print(response)
        except:
            print(f"Failed to retweet {tweet.id}")


printer = TweetPrinterV2(os.environ.get("BEARER_TOKEN"), wait_on_rate_limit=True)

# remove old rules
rule_ids = []
result = printer.get_rules()
print(result)
for rule in result.data:
    print(f"rule marked to delete: {rule.id} - {rule.value}")
    rule_ids.append(rule.id)

if len(rule_ids) > 0:
    printer.delete_rules(rule_ids)
    printer = TweetPrinterV2(os.environ.get("BEARER_TOKEN"))
else:
    print("no rules to delete")

# add new rules
rule_list = ["#techjobs", "#softwarejobs",
             "#careersintech", "#itjobs", "#developerjobs"]
for rule in rule_list:
    rule = StreamRule(value=rule)
    printer.add_rules(rule)

# TODO: lookup docs to get author name/id and see if
#  "cannot retweet" exception is caused by tweet being deleted


printer.filter(expansions="author_id", tweet_fields="created_at")

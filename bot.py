import tweepy
from tweepy import StreamRule

import config
import stream

printer = stream.TweetPrinterV2(config.BEARER_TOKEN)

# clean-up pre-existing rules
rule_ids = []
result = printer.get_rules()
for rule in result.data:
    print(f"rule marked to delete: {rule.id} - {rule.value}")
    rule_ids.append(rule.id)

if len(rule_ids) > 0:
    printer.delete_rules(rule_ids)
    printer = stream.TweetPrinterV2(config.BEARER_TOKEN)
else:
    print("no rules to delete")

# add new rules
# rule = StreamRule(value="Python")


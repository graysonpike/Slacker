# Main Python 3 script to control the Slack bot as an AWS Lambda function

import os
import time
import re
from slackclient import SlackClient

# delay in seconds between reads from RTM
RTM_READ_DELAY = 1
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

# Connect the bot to Slack using the provided OAUTH token
def connect(oauth_token):
    slack_client = SlackClient(oauth_token)
    if slack_client.rtm_connect(with_team_state=False):
        # Read bot's user ID by calling Web API method `auth.test`
        bot_id = slack_client.api_call("auth.test")["user_id"]
        return (slack_client, bot_id)
    else:
        print("Connection failed. Exception traceback printed above.")
        quit()

# Posts a message to the general channel
def post_message(slack_client, bot_id, channel, message):
    slack_client.api_call("chat.postMessage", channel=channel, text=message)


def main():
    event = {
        'channel': 'general',
        'message': 'lamoo'
    }
    context = {

    }
    slack_handler(event, context)

def slack_handler(event, context):
    
    token = os.environ['SLACKBOT_OAUTH_TOKEN']

    channel = event['channel']
    message = event['message']

    print("Posting to #" + channel + ": " + message)

    slack_client, bot_id = connect(token)
    post_message(slack_client, bot_id, "#"+channel, message)

    quit()

main()
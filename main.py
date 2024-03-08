import os

from slackbot import SlackBot

if __name__ == '__main__':
    token = os.environ.get("SLACK_BOT_TOKEN")
    team_id = os.environ.get("SLACK_TEAM_ID")
    if token:
        slackbot = SlackBot(token, team_id)
        print("Got token into webclient")
    else:
        print("Error pulling token!")
        exit(-1)

    # channels = slackbot.get_channels()
    # print(channels)
    # for channel in channels:
    #     print(channel['name'])
    external_users = slackbot.get_external_users()
    for external_user in external_users:
        slackbot.check_channels_for_users(external_user)
    # # slackbot.get_user_groups()
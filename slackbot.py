import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackBot:
    def __init__(self, token, team_id):
        self.token: str = token
        self.team_id: str = team_id
        self.client: WebClient = WebClient(token=self.token)

    def get_channels(self):
        try:
            response = self.client.conversations_list(team_id=self.team_id, types='public_channel,private_channel')
            return response['channels']
        except SlackApiError as e:
            print(e)

    def get_external_users(self):
        try:
            response = self.client.users_list()
            members = response['members']
            external_members = []
            for member in members:
                if 'is_restricted' in member.keys():
                    if member['is_restricted'] is True:
                        external_members.append(member)
                elif 'is_ultra_restricted' in member.keys():
                    if member['is_ultra_restricted'] is True:
                        external_members.append(member)
                else:
                    pass

            return external_members
        except SlackApiError as e:
            print(e)

    def get_user_groups(self):
        try:
            response = self.client.usergroups_list()
            for group in response['usergroups']:
                print(group['name'])
        except SlackApiError as e:
            print(e)

    def check_channels_for_users(self, user):
        try:
            response = self.client.users_conversations(team_id=self.team_id, user=user['id'], types='public_channel,private_channel')
            # if response['channel']:
            for channel in response['channels']:
                # if 'external' not in channel['name']:
                    # print("The following user is in a channel not labeled external!")
                print("Channel: " + channel['name'], user)
                    # print("User: " + user)

        except SlackApiError as e:
            print(e)
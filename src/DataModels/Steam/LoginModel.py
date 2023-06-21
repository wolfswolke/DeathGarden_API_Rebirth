from requests import Response
from datetime import datetime
import json


class FriendsFirstSyncModel:
    steam: bool

    def __init__(self, steam: bool):
        self.steam = steam

    def to_json(self) -> str:
        """Converts class to json string"""
        return json.dumps({"steam": self.steam})


class FixedFriendsUSerPlatformId:
    steam: bool

    def __init__(self, steam: bool):
        self.steam = steam

    def to_json(self) -> str:
        """Converts class to json string"""
        return json.dumps({"steam": self.steam})


class SteamProvider:
    provider_id: str
    provider_name: str
    user_id: str

    def __init__(self, json_object):
        self.provider_id = json_object['providerId']
        self.provider_name = json_object['providerName']
        self.user_id = json_object['userId']

    def to_json(self) -> str:
        """Converts object to json string"""
        return json.dumps(
            {
                "providerId": self.provider_id,
                "providerName": self.provider_name,
                "userId": self.user_id,
            }
        )


class ProviderListEntry:
    provider_name: str
    provider_id: str

    def __init__(self, json_data):
        self.provider_name = json_data['providerName']
        self.provider_id = json_data['providerId']

    def to_json(self) -> str:
        """Converts class to json string"""
        return json.dumps(
            {
                "providerName": self.provider_name,
                "providerId": self.provider_id,
            }
        )


class TriggerResult:
    success: list = []
    error: list = []

    def __init__(self, json_data):
        self.success = json_data['success']
        self.error = json_data['error']

    def to_json(self) -> str:
        """Converts class to json string"""
        return json.dumps(
            {
                "success": self.success,
                "error": self.error,
            }
        )

class SteamLoginResponse:
    # Response Parameters
    preferred_language: str
    friends_first_sync: FriendsFirstSyncModel
    fixed_friends_user_platform_id: FixedFriendsUSerPlatformId
    id: str
    provider: SteamProvider
    providers: list[ProviderListEntry]
    friends: list = []  # not implemented yet, maybe later
    trigger_results: TriggerResult
    token_id: str
    generation_time: datetime
    expiration_time: datetime
    user_id: str
    token: str
    successfully_parsed: bool = False

    def __init__(self, response: Response):
        """ Tries to parse a response to the Model, check if the parse was successfull with is_successfully_parsed()"""

        json_data = json.loads(response.json())
        try:
            self.preferred_language = json_data['preferredLanguage']
            self.friends_first_sync = FriendsFirstSyncModel(json_data['friendsFirstSync']['steam'])
            self.fixed_friends_user_platform_id = FixedFriendsUSerPlatformId(
                json_data['fixedMyFriendsUserPlatformId']['steam'])
            self.id = json_data['id']
            self.provider = SteamProvider(json_data['provider'])

            # Loop over Providers and add them to our array
            providers: list = json_data['providers']
            for entry in providers:
                self.providers.append(ProviderListEntry(entry))

            self.friends = json_data['friends']
            self.trigger_results = json_data['triggerResults']
            self.token_id = json_data['tokenId']
            self.generation_time = datetime.fromtimestamp(json_data['generated'])
            self.expiration_time = datetime.fromtimestamp(json_data['expire'])
            self.user_id = json_data['userId']
            self.token = json_data['token']
            self.successfully_parsed = True

        except TypeError as e:
            print("Could not parse or fully parse Response in SteamLoginResponse Class")

    def is_successfully_parsed(self) -> bool:
        """Returns if the Parsing was successfull"""
        return self.successfully_parsed

    def to_json(self) -> json:
        providers: list = []

        for entry in self.providers:
            providers.append(entry.to_json())

        return_json = {
                "preferredLanguage": self.preferred_language,
                "friendsFirstSync": self.friends_first_sync.to_json(),
                "fixedMyFriendsUserPlatformId": self.fixed_friends_user_platform_id.to_json(),
                "id": self.user_id,
                "provider": self.provider.to_json(),
                "providers": providers,
                "friends": self.friends,
                "triggerResults": self.trigger_results.to_json(),
                "tokenId": self.token_id,
                "generated": self.generation_time.timestamp(),
                "expire": self.expiration_time.timestamp(),
                "userId": self.user_id,
                "token": self.token,
            }
        return json.dumps(return_json)


    @staticmethod
    def get_url(steam_api_key: str, steam_session_token: str, app_id: int):
        return 'https://api.steampowered.com/ISteamUserAuth/AuthenticateUserTicket/v1/?key={}&ticket={}&appid={}'.format(
            steam_api_key, steam_session_token, app_id
        )

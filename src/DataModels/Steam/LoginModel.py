from flask_definitions import *
import requests
from datetime import datetime, timedelta
from logic.mongodb_handler import mongo
import json

global steam_api_key, mongo_db, mongo_host, mongo_collection


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

    def to_json(self) -> str:
        """Converts class to json string"""
        return json.dumps(
            {
                "success": self.success,
                "error": self.error,
            }
        )


class SteamLoginResponse:
    APP_ID = 555440
    APP_ID_SOFTLAUNCH = 854040

    # User id's and tokens
    steam_id: str
    user_id: str
    token: str

    # stuff the game wants
    preferred_language: str = "en"
    friends_first_sync: FriendsFirstSyncModel(True)
    fixed_friends_user_platform_id: FixedFriendsUSerPlatformId(True)

    provider: SteamProvider
    providers: list[ProviderListEntry]

    friends: list = []  # not implemented yet, maybe later
    trigger_results: TriggerResult = TriggerResult()

    generation_time: datetime
    expiration_time: datetime

    __was_successful: bool = False

    def __init__(self, steam_session_token):
        """Makes a request to the steam api and generates a response for the game"""

        try:
            response = requests.get(self.get_url(steam_api_key, steam_session_token, self.APP_ID))

        except TimeoutError as e:
            print("could not reach Steam API.")
            return

        json_body = response.json()

        if "error" in json_body["response"]:
            error_code = json_body["response"]["error"]["errorcode"]
            print("Retrieving Steam ID failed, Error Code:{}, {}".format(
                error_code,
                json_body["response"]["error"]["errordesc"],
            )
            )

            if error_code == 102:
                print("Known error code, trying with alternative App ID")
                response = requests.get(self.get_url(steam_api_key, steam_session_token, self.APP_ID_SOFTLAUNCH))

            else:
                raise Exception(
                    "Could not retrieve users steam ID for unknown reasons\n" +
                    "Steam Response error code: {}\n".format(error_code) +
                    "Error Description: {}".format(json_body["response"]["error"]["errordesc"])
                )

        self.steam_id = response.json()["response"]["params"]["steamid"]

        self.user_id, self.token = mongo.user_db_handler(self.steam_id, mongo_host, mongo_db, mongo_collection)
        self.generation_time = datetime.now()
        self.expiration_time = datetime.now() + timedelta(days=1)

        # Set Provider
        provider: SteamProvider = SteamProvider()
        provider.provider_id = self.steam_id
        provider.provider_name = "steam"
        provider.user_id = self.user_id
        self.provider = provider

        # set Providers Array
        providers_entry: ProviderListEntry = ProviderListEntry()
        providers_entry.provider_id = self.steam_id
        providers_entry.provider_name = "steam"
        self.providers.append(providers_entry)

        logger.graylog_logger(level="info", handler="steam_login", message="User {} logged in".format(self.steam_id))
        # Read: Doc -> AUTH
        # The Client does not validate this and just uses it.

    def to_json(self) -> json:
        if self.__was_successful:
            return json.dumps({"status": "error"})

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
            "tokenId": self.user_id,
            "generated": self.generation_time.timestamp(),
            "expire": self.expiration_time.timestamp(),
            "userId": self.user_id,
            "token": self.token,
        }
        return json.dumps(return_json)

    @staticmethod
    def get_url(api_key: str, steam_session_token: str, app_id: int):
        return 'https://api.steampowered.com/ISteamUserAuth/AuthenticateUserTicket/v1/?key={}&ticket={}&appid={}'.format(
            api_key, steam_session_token, app_id
        )

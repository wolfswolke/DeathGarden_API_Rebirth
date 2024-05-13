import requests


def discord_webhook(urls, data):
    for url in urls:
        requests.post(url, json=data)


class WebhookHandler:
    def __init__(self):
        self.steam_api_key = ""
        self.steam_app_id = ""
        self.steam_url = "https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001"
        self.discord_webhook_url_lobby = ""
        self.discord_webhook_url_reports = ""

    def setup(self, steam_api_key, steam_app_id):
        self.steam_api_key = steam_api_key
        self.steam_app_id = steam_app_id
        #self.discord_webhook_url_lobby = discord_webhook_url_lobby
        #self.discord_webhook_url_reports = discord_webhook_url_reports

    def steam_check_achievments(self, steam_id):
        url = f"{self.steam_url}?appid={self.steam_app_id}&key={self.steam_api_key}&steamid={steam_id}"
        response = requests.get(url)
        return response.json()


webhook_handler = WebhookHandler()

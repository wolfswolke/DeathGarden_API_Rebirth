import requests


def discord_webhook(url, data):
    requests.post(url, json=data)

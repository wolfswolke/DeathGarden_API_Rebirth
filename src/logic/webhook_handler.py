import requests


def discord_webhook(urls, data):
    for url in urls:
        requests.post(url, json=data)

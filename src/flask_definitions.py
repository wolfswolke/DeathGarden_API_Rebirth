from flask import Flask, jsonify, request, send_from_directory, abort, render_template, url_for
from logic.setup_handlers import load_config
from logic.logging_handler import logger
from logic.global_handlers import session_manager
from logic.global_handlers import check_for_game_client
from logic.global_handlers import sanitize_input
from logic.mongodb_handler import mongo
from logic.webhook_handler import discord_webhook
import json
import os

app = Flask(__name__)

config = load_config()
use_graylog = config['graylog']['use']
graylog_server = config['graylog']['host']
steam_api_key = config['steam']['api_key']
mongo_host = config['mongodb']['host']
mongo_db = config['mongodb']['db']
mongo_collection = config['mongodb']['collection']
allowed_tokens = config['api']['allowed_tokens']
discord_mm_url = config['webhooks']['discord']['mm_url']
discord_mm_use = config['webhooks']['discord']['mm_use']
discord_public_url = config['webhooks']['discord']['public_url']
discord_rebirth_url = config['webhooks']['discord']['rebirth_url']

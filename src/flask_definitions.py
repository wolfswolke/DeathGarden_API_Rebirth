from flask import Flask, jsonify, request, send_from_directory, abort, render_template, url_for
from logic.setup_handlers import load_config
from logic.logging_handler import logger
from logic.global_handlers import session_manager
from logic.global_handlers import check_for_game_client
from logic.global_handlers import sanitize_input
from logic.mongodb_handler import mongo
from logic.webhook_handler import discord_webhook
from logic.time_handler import get_lifetime
# from logic.challenge_handler import get_progression_batch, update_progression_batch, get_time_based_challenges
from logic.hash_handler import hash_handler
from logic.challenge_handler_new import new_challenge_handler, get_challenge_ids_from_inventory
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
url_list = config['webhooks']['discord']['url_list']
use_discord = config['webhooks']['discord']['use_discord']
moderation_urls = config['webhooks']['discord']['moderation_urls']
dev_env = os.environ['DEV']

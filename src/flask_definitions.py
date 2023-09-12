from flask import Flask, jsonify, request, send_from_directory, abort, render_template, url_for
from logic.setup_handlers import load_config
from logic.logging_handler import logger
from logic.global_handlers import session_manager
from logic.global_handlers import check_for_game_client
from logic.mongodb_handler import mongo
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

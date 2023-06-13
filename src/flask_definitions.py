from flask import Flask, jsonify, request, send_from_directory, abort
from logic.global_handlers import get_remote_ip, load_config
from logic.logging_handler import graylog_logger

app = Flask(__name__)

config = load_config()
use_graylog = config['graylog']['use']
graylog_server = config['graylog']['host']
steam_api_key = config['steam']['api_key']
mongo_host = config['mongodb']['host']
mongo_db = config['mongodb']['db']
mongo_collection = config['mongodb']['collection']
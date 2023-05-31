from datetime import datetime, date
from elasticsearch import Elasticsearch
import json


def es_upload(server, index, log_message):
    if type(log_message) is not dict:
        log_message = {"steam_key": log_message}
    log_message["timestamp"] = datetime.utcnow().isoformat()
    es = Elasticsearch(server)
    data = json.dumps(log_message)
    response = es.index(index=index, body=data, headers={'Content-Type': 'application/json;charset=UTF-8'})
    document_id = response['_id']
    print("Uploaded dictionary with ID:", document_id)

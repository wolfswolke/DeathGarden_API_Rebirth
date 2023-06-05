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


def dev_es_upload(server, index, log_message):
    if index == "client_event":
        playerUniqueId = log_message["playerUniqueId"]
        clientEvent = log_message["clientEvent"]
        eventType = log_message["eventType"]
        timestamp = datetime.utcnow().isoformat()
        upload_string = "Message: {}. Sender: {}.".format(clientEvent, playerUniqueId)
        upload_message = {"msg_type": "error", "timestamp": timestamp, "message": upload_string, "type": "string"}
        es = Elasticsearch(server)
        response = es.index(index="dev_client_event", body=upload_message)
        document_id = response['_id']
        print("Uploaded dictionary with ID:", document_id)

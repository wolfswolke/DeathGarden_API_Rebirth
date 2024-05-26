from flask_definitions import *
import time
import uuid
import os
import json


class FileHandler:
    def __init__(self):
        self.file_path = "/app/tmp/uploads/"
        self.metadata_file = "metadata.json"
        self.metadata_file_path = f"{self.file_path}{self.metadata_file}"
        self.metadata = {}

    def setup(self):
        if not os.path.exists(self.file_path):
            os.makedirs(self.file_path)
            logger.graylog_logger(level="info", handler="file_handler", message=f"File Path: {self.file_path} created.")
        if not os.path.exists(self.metadata_file_path):
            with open(self.metadata_file_path, "w") as metadata_file:
                metadata_file.write("{}")
            logger.graylog_logger(level="info", handler="file_handler",
                                  message=f"Metadata File: {self.metadata_file_path} created.")
        with open(self.metadata_file_path, "r") as metadata_file:
            self.metadata = json.load(metadata_file)
            logger.graylog_logger(level="info", handler="file_handler", message=f"Metadata Loaded: {self.metadata}")
    def save_metadata(self):
        with open(self.metadata_file_path, "w") as metadata_file:
            json.dump(self.metadata, metadata_file)

    def create_file(self, file, user_id):
        file_id = str(uuid.uuid4())
        file.save(f"{self.file_path}{file_id}")
        sha256 = hash_handler.get_256_sum(f"{self.file_path}{file_id}")
        self.metadata[file_id] = {"file_id": file_id, "user_id": user_id, "sha256": sha256, "created": time.time()}
        logger.graylog_logger(level="info",
                              handler="file_handler",
                              message=f"File: {file_id} created by User: {user_id} with SHA256: {sha256}")
        self.save_metadata()
        return file_id

    def get_file(self, file_id):
        if file_id not in self.metadata:
            return None
        return send_from_directory(self.file_path, file_id)

    def get_file_sha256(self, file_id):
        if file_id not in self.metadata:
            return None
        return self.metadata[file_id]["sha256"]

    def get_metadata(self, file_id):
        if file_id not in self.metadata:
            return None
        return self.metadata[file_id]


file_handler = FileHandler()
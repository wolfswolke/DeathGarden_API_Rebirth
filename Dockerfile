FROM python:3.13.0a6-alpine3.18

RUN apk upgrade && apk add curl
# copying each folder one by one so docker can cache the layers
#COPY . /app
RUN mkdir -p /app/
RUN mkdir -p /app/src
RUN mkdir -p /app/src/logic

WORKDIR /app/src

COPY requirements.txt /app/src/requirements.txt
RUN pip install -r requirements.txt
RUN pip install --upgrade pip

COPY src/start_app.py /app/src/start_app.py
COPY src/flask_definitions.py /app/src/flask_definitions.py

COPY src/config/ /app/src/config/

COPY src/endpoints/general.py /app/src/endpoints/general.py
COPY src/endpoints/logging.py /app/src/endpoints/logging.py
COPY src/endpoints/matchmaking.py /app/src/endpoints/matchmaking.py
COPY src/endpoints/unknown.py /app/src/endpoints/unknown.py
COPY src/endpoints/user_handeling.py /app/src/endpoints/user_handeling.py
COPY src/endpoints/web.py /app/src/endpoints/web.py

COPY src/files/ /app/src/files/
COPY src/image/ /app/src/image/
COPY src/json/ /app/src/json/
COPY src/static/ /app/src/static/
COPY src/templates/ /app/src/templates/
COPY src/util/ /app/src/util/

# Copy logic
COPY src/logic/challenge_handler.py /app/src/logic/challenge_handler.py
COPY src/logic/challenge_handler_new.py /app/src/logic/challenge_handler_new.py
COPY src/logic/file_handler.py /app/src/logic/file_handler.py
COPY src/logic/global_handlers.py /app/src/logic/global_handlers.py
COPY src/logic/hash_handler.py /app/src/logic/hash_handler.py
COPY src/logic/level_handler.py /app/src/logic/level_handler.py
COPY src/logic/logging_handler.py /app/src/logic/logging_handler.py
COPY src/logic/mongodb_handler.py /app/src/logic/mongodb_handler.py
COPY src/logic/queue_handler.py /app/src/logic/queue_handler.py
COPY src/logic/setup_handlers.py /app/src/logic/setup_handlers.py
COPY src/logic/time_handler.py /app/src/logic/time_handler.py
COPY src/logic/webhook_handler.py /app/src/logic/webhook_handler.py
COPY src/logic/presence_handler.py /app/src/logic/presence_handler.py

EXPOSE 8080

HEALTHCHECK CMD curl --fail http://localhost:8080/api/v1/healthcheck

ENTRYPOINT ["python", "start_app.py"]

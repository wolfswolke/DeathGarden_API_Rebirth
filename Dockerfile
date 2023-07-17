FROM python:3.12.0b4-alpine3.18

COPY . /app
COPY requirements.txt /app/src

WORKDIR /app/src

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN apk add curl

EXPOSE 8080

HEALTHCHECK CMD curl --fail http://localhost:8080/

ENTRYPOINT ["python", "start_app.py"]

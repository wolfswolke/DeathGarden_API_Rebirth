FROM python:3.10-alpine
COPY . /app
COPY requirements.txt /app/src

WORKDIR /app/src

RUN pip install -r requirements.txt

RUN apk add curl

EXPOSE 8080

HEALTHCHECK CMD curl --fail http://localhost:8080/

ENTRYPOINT ["python", "start_app.py"]

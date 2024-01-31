FROM python:3.13.0a3-alpine3.18

RUN apk upgrade && apk add curl && apk upgrade busybox # CVE-2022-48174

COPY . /app/
COPY requirements.txt /app/src/requirements.txt

WORKDIR /app/src

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8080

HEALTHCHECK CMD curl --fail http://localhost:8080/api/v1/healthcheck

ENTRYPOINT ["python", "start_app.py"]

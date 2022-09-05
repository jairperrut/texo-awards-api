FROM python:3.10.5-slim-buster

WORKDIR /app

COPY . .

EXPOSE 8000

RUN pip install -r requirements.txt

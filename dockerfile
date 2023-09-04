FROM python:3.10-slim-bullseye

RUN apt-get update \
  && pip install --no-cache-dir --upgrade pip\
  && pip install requests pymongo

WORKDIR /python_dev
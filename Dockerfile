FROM python:3.11-slim-buster
ENV PYTHONUNBUFFERED=1
LABEL authors="davilos"

WORKDIR /django

COPY requirements.txt /django/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /django

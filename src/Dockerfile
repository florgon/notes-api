# syntax=docker/dockerfile:1
FROM python:3.10.4-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /web/notes
COPY requirements.txt /web/notes/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /web/notes/
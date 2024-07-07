FROM python:3.9.11

ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY requirements.txt /backend/

RUN pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install -r requirements.txt \
    && pip install django-extensions \
    && pip install python-dotenv

RUN pip install nba_api

COPY . /backend/
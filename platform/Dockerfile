FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /platform

WORKDIR /platform

ADD . /platform/

RUN pip install -r requirements.txt

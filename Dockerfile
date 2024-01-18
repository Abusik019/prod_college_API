FROM python:3.10-alpine3.19

COPY requirements.txt /temp/requirements.txt
COPY college_API /college_API

WORKDIR /college_API
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password zabit923

USER zabit923


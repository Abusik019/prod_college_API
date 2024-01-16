FROM python:3.10-slim

RUN mkdir /project
WORKDIR /project

ADD . /project/
ADD .env.docker /project/.env

RUN pip install -r requirements.txt

CMD ["gunicorn", "config.wsgi:application", "-b", "0.0.0.0:8000"]

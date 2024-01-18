FROM python:3.10-slim

RUN mkdir /project
WORKDIR /project/

COPY . /project/

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]


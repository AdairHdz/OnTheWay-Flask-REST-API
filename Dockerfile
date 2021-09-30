FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

WORKDIR /app/flaskr

CMD [ "flask", "run", "--host=0.0.0.0"]
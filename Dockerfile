FROM python:latest

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

COPY . .


EXPOSE 8000


CMD gunicorn pro1.wsgi:application -b 0.0.0.0:8000 -w 1 -t 300
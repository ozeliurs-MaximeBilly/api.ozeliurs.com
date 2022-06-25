FROM python:3.7.3-slim

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY ./www /app

WORKDIR /app

ENTRYPOINT ["./gunicorn_starter.sh"]
FROM python:3.7.3-slim

COPY ./www /app

RUN pip3 install -r /app/requirements.txt

WORKDIR /app

ENTRYPOINT ["./gunicorn_starter.sh"]
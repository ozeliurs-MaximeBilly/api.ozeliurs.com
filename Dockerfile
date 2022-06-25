FROM python:3.7.3-slim

COPY ./www /app

RUN chmod 777 /app

RUN pip3 install -r /app/requirements.txt

WORKDIR /app

ENTRYPOINT ["/app/gunicorn_starter.sh"]
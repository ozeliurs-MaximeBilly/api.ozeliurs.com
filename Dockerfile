FROM alpine:latest

RUN apk add --update python3 python3-pip

COPY ./www /app

RUN chmod 777 /app

RUN pip3 install -r /app/requirements.txt

WORKDIR /app

ENTRYPOINT ["/app/gunicorn_starter.sh"]
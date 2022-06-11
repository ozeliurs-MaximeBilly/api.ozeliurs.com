import json
import random
import time
import requests
from bs4 import BeautifulSoup as bs
from flask import Flask, jsonify, request, redirect, url_for
from pathlib import Path
from hashlib import md5

app = Flask(__name__)

# PRELOAD ----------
with open("/var/www/api/ipout", "r", encoding="utf8") as csv:
    csv = [[x for x in line.split(" ")] for line in csv.read().split("\n")[:-1]]


@app.route("/")
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/cfb/<site>")
def cloudflare_bypass(site: str):
    output = [x for x in csv if site in x[1]]

    return jsonify(output)


@app.route("/fake/")
def fake():
    soup = bs(requests.get("http://www.lorraine-ipsum.fr").text)

    try:
        fake_ids = json.loads(Path("/var/www/api/funny.json").read_text())
    except:
        fake_ids = []

    ul = soup.find("ul", {"id": "list_matches"})
    for li in ul.findAll("li"):
        surname = li.find("span", {"class": "name"}).text
        name = li.find("span", {"class": "word"}).text

        if {"surname":surname, "name":name} not in fake_ids:
            fake_ids.append({"surname":surname, "name":name})

    Path("/var/www/api/funny.json").write_text(json.dumps(fake_ids, indent=4))

    return jsonify({"surname":surname,
                    "name":name,
                    "profile_picture": "https://api.ozeliurs.com" + url_for('static', filename=f"raccoons/raccoon-{random.randrange(1, 200)}.jpg")})


@app.route("/imdb/", defaults={'u_path': ''})
@app.route('/imdb/<path:u_path>')
def imdb_cache(u_path: str):
    cache = json.loads(Path("/var/www/api/imdb_cache.json").read_text())
    u_path_hash = md5(u_path.encode()).hexdigest()
    if u_path_hash in cache:
        return cache[u_path_hash]
    else:
        req = requests.get(f"https://imdb-api.com/{u_path}")
        if req.json()["errorMessage"] == "":
            cache[u_path_hash] = req.text
            Path("/var/www/api/imdb_cache.json").write_text(json.dumps(cache, indent=4))

        return req.text


if __name__ == '__main__':
    app.run()

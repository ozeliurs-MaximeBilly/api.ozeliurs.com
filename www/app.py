import json
import random
import time
import requests
from bs4 import BeautifulSoup as bs
from flask import Flask, jsonify, request, redirect, url_for
from pathlib import Path

app = Flask(__name__)


@app.route("/")
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/hothothot/")
def hothothot():
    with open("/data/hothothot.log", "r", encoding="utf8") as log:
        hist = log.read()
        
    return jsonify(json.loads(hist.split("\n")[-2]))


@app.route("/hothothot/hist/")
def hothothot_hist():
    with open("/data/hothothot.log", "r", encoding="utf8") as log:
        hist = log.read()
        hist = [json.loads(x) for x in hist.split("\n")[-48:-1]]
    
    return jsonify(hist)


@app.route("/<identifier>.css")
def identify(identifier):
    print(request.remote_addr)
    with open("/data/access.csv", "a", encoding="utf8") as log:
        log.write(f"\n{identifier}, {time.time()}, {request.remote_addr}")
    return redirect(url_for("static", filename="style.css"))


@app.route("/fake/")
def fake():
    soup = bs(requests.get("http://www.lorraine-ipsum.fr").text)

    try:
        fake_ids = json.loads(Path("/data/funny.json").read_text())
    except:
        fake_ids = []

    ul = soup.find("ul", {"id": "list_matches"})
    for li in ul.findAll("li"):
        surname = li.find("span", {"class": "name"}).text
        name = li.find("span", {"class": "word"}).text

        if {"surname":surname, "name":name} not in fake_ids:
            fake_ids.append({"surname":surname, "name":name})

    Path("/data/funny.json").write_text(json.dumps(fake_ids, indent=4))

    return jsonify({"surname":surname,
                    "name":name,
                    "profile_picture": "https://api.ozeliurs.com" + url_for('static', filename=f"raccoons/raccoon-{random.randrange(1, 200)}.jpg")})


@app.route("/imdb/", defaults={'u_path': ''})
@app.route('/imdb/<path:u_path>')
def imdb_cache(u_path: str):
    cache = json.loads(Path("/data/imdb_cache.json").read_text())
    if u_path.__hash__() in cache:
        return cache[u_path.__hash__()]
    else:
        req = requests.get(f"https://imdb-api.com/{u_path}")
        if req.json()["errorMessage"] == "":
            cache[u_path.__hash__()] = req.text
            Path("/data/imdb_cache.json").write_text(json.dumps(cache, indent=4))

        return req.text


if __name__ == '__main__':
    app.run()

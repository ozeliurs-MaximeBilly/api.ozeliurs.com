import json
import time
import requests
from bs4 import BeautifulSoup as bs
from flask import Flask, jsonify, request, redirect, url_for

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

    ul = soup.find("ul", {"id": "list_matches"})
    li = ul.find("li")
    surname = li.find("span", {"class": "name"}).text
    name = li.find("span", {"class": "word"}).text

    return jsonify({"surname":surname, "name":name})


if __name__ == '__main__':
    app.run()

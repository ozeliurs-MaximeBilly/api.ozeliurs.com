import json
import time
from flask import Flask, jsonify, request, redirect

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


@app.route("/allumes/")
def allumes():
    with open("/data/allumes.log", "r", encoding="utf8") as log:
        hist = log.read()

    return jsonify(json.loads(hist.split("\n")[-2]))


@app.route("/allumes/hist/")
def allumes_hist():
    with open("/data/allumes.log", "r", encoding="utf8") as log:
        hist = log.read()
        hist = [json.loads(x) for x in hist.split("\n")[:-1]]
        
        
@app.route("/allumes/last/")
def allumes_last():
    with open("/data/allumes.log", "r", encoding="utf8") as log:
        hist = log.read()
        hist = [json.loads(x) for x in hist.split("\n")[-288:-1]]

    return jsonify(hist)

@app.route("/<id>.css")
def identify(identifier):
    print(request.remote_addr)
    with open("/data/access.csv", "a", encoding="utf8") as log:
        log.write(f"\n{identifier}, {time.time()}, {request.remote_addr}")
    return redirect("/static/style.css")


if __name__ == '__main__':
    app.run()

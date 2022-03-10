import json

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/hothothot/capteurs')
def hothothot():
    with open("hothothot.log", "r", encoding="utf8") as log:
        hist = log.read()
        
    return jsonify(json.loads(hist.split("\n")[-1]))


@app.route('/hothothot/hist')
def hothothot_hist():
    with open("hothothot.log", "r", encoding="utf8") as log:
        hist = log.read()
        hist = [json.loads(x) for x in hist.split("\n")[-48:]]
    
    return jsonify(hist)


if __name__ == '__main__':
    app.run()

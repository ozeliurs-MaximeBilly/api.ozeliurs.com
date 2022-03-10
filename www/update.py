import requests

with open("/data/hothothot.log", "a", encoding="utf8") as log:
  log.write(requests.get("https://hothothot.dog/api/capteurs/").text)

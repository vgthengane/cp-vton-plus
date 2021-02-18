import json

with open("config.json") as f:
    params = json.load(f)

HEIGHT = params["HEIGHT"]
WIDTH = params["WIDTH"]
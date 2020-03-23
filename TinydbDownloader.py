import requests
import json

base_url = "https://tinydb.eiphax.tech/api"

apps = requests.get(f"{base_url}/apps").text
apps_json = json.loads(apps)
for app in apps_json:
    if app["cia"]:
        id = app["id"]
        name = app["name"]
        headline = app["headline"]
        print(f"ID {id}: {name} | {headline}")
    else:
        pass
choices = input("Choose app id(s) to download in a comma separated list:").replace(" ", "").split(",")
for choice in choices:
    download_url = json.loads(requests.get(f"{base_url}/apps?app_id={choice}").text)[0]["cia"][-1]["download_url"]
    cia_file = requests.get(download_url)
    open(download_url.split("/")[-1], "wb").write(cia_file.content)
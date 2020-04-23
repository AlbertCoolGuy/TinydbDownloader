import requests
import json
import re

base_url = "https://tinydb.eiphax.tech/api"

apps = requests.get(f"{base_url}/apps").text
apps_json = json.loads(apps)

def list_all_apps():
    for app in apps_json:
        if app["cia"]:
            id = app["id"]
            name = app["name"]
            headline = app["headline"]
            last_updated = str(app["cia"][-1]["mtime"])[0:9]
            print(f"ID {id}: {name} | {headline} | Last updated: {last_updated}")
        else:
            pass

def search_for_app(search):
    for app in apps_json:
        if re.search(search, app["name"], re.IGNORECASE):
            if app["cia"]:
                id = app["id"]
                name = app["name"]
                headline = app["headline"]
                print(f"ID {id}: {name} | {headline}")
            else:
                pass
        else:
            pass
   
def option():
    while True:   
        choice = input("What do you want to do? (L)ist all apps, (S)earch for a app or (Q)uit the program:")
        if choice.lower() == "l":
            list_all_apps()
            download()
        elif choice.lower() == "s":
            search_for_app(input("Enter a string to search for:"))
            download()
        elif choice.lower() == "q":
            print("Quitting")
            break
        else:
            print("Invalid choice, try again.")

def download():
    while True:
        ids = input("Choose app id(s) to download in a comma separated list:").replace(" ", "").split(",")
        for id in ids:
            if id.isnumeric():
                    try:
                        download_url = json.loads(requests.get(f"{base_url}/apps?app_id={id}").text)[0]["cia"][-1]["download_url"]
                        cia_file = requests.get(download_url)
                        open(download_url.split("/")[-1], "wb").write(cia_file.content)
                    except IndexError:
                        print("Invalid id, try again.")
            else:
                    print("Input is not a number.")
            

option()            
download()

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
            print(f"ID {id}: {name} | {headline}")
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
    choice = input("What do you want to do? (L)ist all apps or (S)earch for a app:")
    if choice.lower() == "l":
        list_all_apps()
    elif choice.lower() == "s":
        search_for_app(input("Enter a string to search for:"))
    else:
        print("Invalid choice, try again.")
        option()
        

def download():
    ids = input("Choose app id(s) to download in a comma separated list:").replace(" ", "").split(",")
    for id in ids:
        try:    
            download_url = json.loads(requests.get(f"{base_url}/apps?app_id={id}").text)[0]["cia"][-1]["download_url"]
            cia_file = requests.get(download_url)
            open(download_url.split("/")[-1], "wb").write(cia_file.content)
        except IndexError:
            print("Invalid id, try again.")
            download()
            

option()            
download()

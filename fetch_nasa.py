import requests
import os
import datetime
from dotenv import load_dotenv
from url_split import url_split


def fetch_nasa_apod(apod_links):
    payload = {
        "api_key": nasa_api_key,
        "start_date": "2016-01-01",
        "end_date": "2016-02-02",
    }
    response = requests.get(nasa_apod_url,params=payload)
    response.raise_for_status()
    apod = response.json()
    for links in apod:
        apod_links.append(links["url"])
    for number, images in enumerate(apod_links, 1):
        response = requests.get(images)
        response.raise_for_status()
        extension = url_split(images)
        with open(os.path.join(directory, f"nasa apod{number}{extension}"), "wb") as file:
            file.write(response.content)


def fetch_nasa_epic(epic_images):
    payload = {
        "api_key":"DEMO_KEY"
    }
    response = requests.get(nasa_epic_url,params=payload)
    response.raise_for_status()
    epics = response.json()
    for epic in epics:
        adatetime = datetime.datetime.fromisoformat(epic["date"])
        formatted_date = adatetime.strftime("%Y/%m/%d")
        epic_images.append(epic["image"])
    payload= {
        "api_key":nasa_api_key
        }
    for number, image in enumerate(epic_images, 1):
        response = requests.get(f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{image}.png",params=payload)
        response.raise_for_status()
        epic_link = response.url
        extension = url_split(epic_link)
        with open(os.path.join(directory, f"nasa epic{number}{extension}"), "wb") as file:
            file.write(response.content)


if __name__ == "__main__":
    directory = input("Введите название папки ")
    os.makedirs(directory,exist_ok=False)
    nasa_apod_url = "https://api.nasa.gov/planetary/apod"
    nasa_epic_url = "https://api.nasa.gov/EPIC/api/natural/date/2019-05-30"
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")
    apod_links = []
    epic_images = []
    fetch_nasa_apod(apod_links)
    fetch_nasa_epic(epic_images)

import requests
import os
import datetime
from dotenv import load_dotenv
from url_split_and_dowland_images import url_split, download_image


def fetch_nasa_apod(directory):
    payload = {
        "api_key": nasa_api_key,
        "start_date": "2016-01-01",
        "end_date": "2016-02-02",
    }
    nasa_apod_url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(nasa_apod_url, params=payload)
    response.raise_for_status()
    apod = response.json()
    apod_links = []
    for links in apod:
        apod_links.append(links["url"])
    for number, image in enumerate(apod_links, 1):
        extension = url_split(images)
        path = (directory, f"nasa apod{number}{extension}")
        download_image(path, image)


def fetch_nasa_epic(directory):
    payload = {"api_key": nasa_api_key}
    nasa_epic_url = "https://api.nasa.gov/EPIC/api/natural/date/2019-05-30"
    response = requests.get(nasa_epic_url, params=payload)
    response.raise_for_status()
    epics = response.json()
    epic_images = []
    for epic in epics:
        adatetime = datetime.datetime.fromisoformat(epic["date"])
        formatted_date = adatetime.strftime("%Y/%m/%d")
        epic_images.append(epic["image"])
    for number, image in enumerate(epic_images, 1):
        nasa_epic_link = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{image}.png"
        extension = url_split(nasa_epic_link)
        path = os.path.join(directory, f"nasa epic{number}{extension}")
        download_image(path, nasa_epic_link, payload=payload)


if __name__ == "__main__":
    directory = input("Введите название папки ")
    os.makedirs(directory, exist_ok=False)
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")
    fetch_nasa_apod(directory)
    fetch_nasa_epic(directory)

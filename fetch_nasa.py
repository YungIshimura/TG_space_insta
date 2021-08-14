import requests
import os
import urllib
import datetime
from dotenv import load_dotenv


def url_split(url):
    url_slpit = urllib.parse.urlsplit(url)
    path = url_slpit[2]
    return os.path.splitext(path)[1]


def fetch_nasa_APOD(APOD_links):
    payload = {
        "api_key": nasa_api_key,
        "start_date": "2016-01-01",
        "end_date": "2016-02-02",
    }
    response = requests.get(nasa_APOD_url,params=payload)
    response.raise_for_status
    APOD = response.json()
    for links in APOD:
        APOD_links.append(links["url"])
    for number, images in enumerate(APOD_links, 1):
        response = requests.get(images)
        extension = url_split(images)
        with open(os.path.join(direc, "nasa APOD"f'{number}{extension}'), "wb") as file:
            file.write(response.content)


def fetch_nasa_EPIC(EPIC_images):
    payload = {
        "api_key":"DEMO_KEY"
    }
    response = requests.get(nasa_EPIC_url,params=payload)
    EPICs = response.json()
    for EPIC in EPICs:
        aDateTime = datetime.datetime.fromisoformat(EPIC["date"])
        formatted_date = aDateTime.strftime("%Y/%m/%d")
        EPIC_images.append(EPIC["image"])
    payload = {"api_key": nasa_api_key}
    for number, image in enumerate(EPIC_images, 1):
        response = requests.get(
            "https://api.nasa.gov/EPIC/archive/natural,"f"{'/'}{formatted_date}{'/png'}{'/'}{image}{'.png'}",
            params=payload
        )
        EPIC_link = response.url
        extension = url_split(EPIC_link)
        with open(os.path.join(direc, f'{"nasa EPIC "}{number}{extension}'), "wb") as file:
            file.write(response.content)


if __name__=='__main__':
    direc = input("Введите название папки ")
    os.makedirs(direc,exist_ok=False)
    nasa_APOD_url = "https://api.nasa.gov/planetary/apod"
    nasa_EPIC_url = "https://api.nasa.gov/EPIC/api/natural/date/2019-05-30"
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")
    APOD_links = []
    EPIC_images = []
    fetch_nasa_APOD(APOD_links)
    fetch_nasa_EPIC(EPIC_images)

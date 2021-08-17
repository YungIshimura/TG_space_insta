import requests
import os
from dotenv import load_dotenv
from url_split import url_split

def fetch_spacex_last_launch():
    response = requests.get("https://api.spacexdata.com"f'{"/v3"}{"/launches"}')
    response.raise_for_status()
    launches = response.json()
    images_links = launches[15]["links"]["flickr_images"]
    for number, images in enumerate(images_links, 1):
        extension = url_split(images)
        response = requests.get(images)
        response.raise_for_status()
        with open(os.path.join(directory, f"spacex image{number}{extension}"), "wb") as file:
            file.write(response.content)


if __name__ == "__main__":
    directory = input("Введите название папки ")
    os.makedirs(directory,exist_ok=False)
    fetch_spacex_last_launch()
    
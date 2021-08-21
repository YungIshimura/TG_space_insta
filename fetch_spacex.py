import requests
import os
from dotenv import load_dotenv
from url_split_and_dowland_images import url_split, download_image


def fetch_spacex_last_launch(directory):
    response = requests.get("https://api.spacexdata.com" f'{"/v3"}{"/launches"}')
    response.raise_for_status()
    launches = response.json()
    images_links = launches[15]["links"]["flickr_images"]
    for number, image in enumerate(images_links, 1):
        extension = url_split(image)
        path = os.path.join(directory, f"spacex image{number}{extension}")
        download_image(path, image)


if __name__ == "__main__":
    directory = input("Введите название папки ")
    os.makedirs(directory, exist_ok=False)
    fetch_spacex_last_launch(directory)

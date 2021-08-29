import requests
import os
from dotenv import load_dotenv
from get_file_extension_and_dowland_images import get_file_extension, download_image


def fetch_spacex_last_launch(directory):
    response = requests.get("https://api.spacexdata.com/v3/launches")
    response.raise_for_status()
    launches = response.json()
    images_links = launches[15]["links"]["flickr_images"]
    
    for number, image in enumerate(images_links, 1):
        extension = get_file_extension(image)
        path = os.path.join(directory, f"spacex image{number}{extension}")
        download_image(path, image)


if __name__ == "__main__":
    directory = input("Введите название папки ")
    os.makedirs(directory, exist_ok=False)
    fetch_spacex_last_launch(directory)

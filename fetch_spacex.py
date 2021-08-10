import requests
import os
import urllib
from dotenv import load_dotenv


def url_split(url):
    url_slpit = urllib.parse.urlsplit(url)
    path = url_slpit[2]
    return os.path.splitext(path)[1]


def fetch_spacex_last_launch():
    response = requests.get(f'{url}{"/v3"}{"/launches"}')
    launches = response.json()
    images_links = launches[15]["links"]["flickr_images"]
    for number, images in enumerate(images_links, 1):
        response = requests.get(images)
        extension = url_split(images)
        with open(os.path.join(direc, f'{"spacex image "}{number}{extension}'), "wb") as file:
            file.write(response.content)


if __name__=='__main__':
    direc = input("Введите название папки ")
    try:
        os.mkdir(direc)
    except FileExistsError:
        print('Такая папка уже создана')
    url = "https://api.spacexdata.com"
    fetch_spacex_last_launch()
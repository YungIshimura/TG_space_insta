import os
import urllib
import requests


def url_split(url):
    url = urllib.parse.unquote(url)
    url_slpit = urllib.parse.urlsplit(url)
    path = url_slpit[2]
    return os.path.splitext(path)[1]


def download_image(path, url):
        response = requests.get(url)
        response.raise_for_status()
        with open(path, "wb") as file:
            file.write(response.content)
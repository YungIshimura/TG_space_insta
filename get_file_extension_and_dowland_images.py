import os
import urllib
import requests


def get_file_extension(url):
    url = urllib.parse.unquote(url)
    url_slpit = urllib.parse.urlsplit(url)
    path = url_slpit[2]
    return os.path.splitext(path)[1]


def download_image(path, url, payload=None):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(path, "wb") as file:
        file.write(response.content)


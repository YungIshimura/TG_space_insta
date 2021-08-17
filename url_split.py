import os
import urllib


def url_split(url):
    url = urllib.parse.unquote(url)
    url_slpit = urllib.parse.urlsplit(url)
    path = url_slpit[2]
    return os.path.splitext(path)[1]
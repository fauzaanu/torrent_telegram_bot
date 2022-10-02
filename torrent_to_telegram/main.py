import json
import os

import requests
from shorten import shorten


def torrent_downloader_as(magnet_url):
    returnlist = {}
    url = "https://webtor.p.rapidapi.com/resource"

    payload = magnet_url
    headers = {
        "content-type": "text/plain",
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "webtor.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    content_id = response.json()['id']

    url = f"https://webtor.p.rapidapi.com/resource/{content_id}/list"

    querystring = {"path": "/", "limit": "10", "offset": "0"}

    headers = {
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "webtor.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    for item in response.json()['items']:
        resource_id = item['id']
        # print(resource_id)
        url = f"https://webtor.p.rapidapi.com/resource/{content_id}/export/{resource_id}"

        headers = {
            "X-RapidAPI-Key": "",
            "X-RapidAPI-Host": "webtor.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)

        download_link = response.json()["exports"]["download"]["url"]
        file_name = response.json()["source"]["name"]
        print(type(download_link))
        print(download_link)


        returnlist[file_name] = shorten(str(download_link))
    print(returnlist)
    return returnlist

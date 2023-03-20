import requests
import pandas as pd


class Unsplash:
    def __init__(self):
        self.url = "https://api.unsplash.com/"
        self.client_id = ""  # YOUR CLIENT ID HERE

    @staticmethod
    def request(url, params):
        response = requests.get(url=url, params=params)
        return response

    @staticmethod
    def json_formatter(data):
        photos_info = {
            "alt_description": [],
            "created_at": [],
            "username": [],
            "image_link": [],
            "download_link": [],
            "likes": [],
        }

        for i in range(len(data)):
            photos_info["alt_description"].append(data[i]["alt_description"])
            photos_info["created_at"].append(data[i]["created_at"])
            photos_info["username"].append(data[i]["user"]["name"])
            photos_info["image_link"].append(data[i]["urls"]["raw"])
            photos_info["download_link"].append(data[i]["links"]["download"])
            photos_info["likes"].append(data[i]["likes"])

        return photos_info

    @staticmethod
    def df_formatter(data):
        df = pd.DataFrame(data)
        return df

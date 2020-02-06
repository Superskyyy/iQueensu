"""
This file sets the credentials and other options for the SOLUS spider
"""
import json
import os
import sys

SCRAPER_USER_NAME, SCRAPER_USER_PASSWD = "", ""
try:
    with open("QCumber/scraper/assets/spider_credentials.json") as credentials_file:
        credentials = json.load(credentials_file)
        SCRAPER_USER_NAME = credentials["username"]
        SCRAPER_USER_PASSWD = credentials["password"]
except FileNotFoundError:
    print("spider_credentials.json File not found, make sure it's set from Admin site")
SCRAPER_DEBUG = True
SCRAPER_LOCAL_TEST = True


class Settings:
    """
    Path finders
    """

    def __init__(self, driver_path):
        self.data = dict()
        self.data["driver_path"] = driver_path

    def load_from_file(self, path="QCumber_Scraper_Config.json"):
        with open(self.purify_path(os.path.join(sys.path[0], path)), "r+") as file:
            self.data = json.load(file)

    def save_to_file(self, path="QCumber_Scraper_Config.json"):
        with open(self.purify_path(os.path.join(sys.path[0], path)), "w+") as file:
            json.dump(self.data, file)

    def purify_path(self, path):
        return os.path.normpath(os.path.abspath(path))

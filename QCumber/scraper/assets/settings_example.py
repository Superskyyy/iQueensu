import json
import os
import sys

SCRAPER_DEBUG = True
SCRAPER_LOCAL_TEST = True
SCRAPER_USER_NAME = 'your user name'  # Edit this
SCRAPER_USER_PASSWD = 'your passwd'  # Edit this

SCRAPER_DRIVER = 'geckodriver'  # Set workable driver name here

SCRAPER_DB_CREDENTIALS = {  # Edit this, the db system should be PostgreSQL.
    "database": "",
    "host": "",
    "port": "",
    "username": "",
    "password": ""
}


class Settings:
    def __init__(self, driver_path):
        self.data = dict()
        self.data['driver_path'] = driver_path

    def load_from_file(self, path='QCumber_Scraper_Config.json'):
        with open(self.purify_path(os.path.join(sys.path[0], path)), 'r+') as file:
            self.data = json.load(file)

    def save_to_file(self, path='QCumber_Scraper_Config.json'):
        with open(self.purify_path(os.path.join(sys.path[0], path)), 'w+') as file:
            json.dump(self.data, file)

    @staticmethod
    def purify_path(path):
        return os.path.normpath(os.path.abspath(path))

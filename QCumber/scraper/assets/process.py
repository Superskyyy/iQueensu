import io
import json


class Process:
    __procedure: json

    def __init__(self, driver):
        self.__driver = driver

    def load(self, json_path: str):
        with io.open(json_path, 'r') as json_file:
            self.__procedure = json.load(json_file)
        return self

    def run(self):
        print(self.__procedure)

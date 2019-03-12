import io
import json
from selenium.common.exceptions import NoSuchElementException


# Because of some problem, this function stop to develop for now.

class Process:
    __procedure: json

    def __init__(self, driver):
        self.__driver = driver

    def load(self, json_path: str):
        with io.open(json_path, 'r') as json_file:
            self.__procedure = json.load(json_file)
        return self

    def run(self):
        for steps in self.__procedure:
            getattr(self, steps['type'])(steps['action'])

    def dismiss(self, elements):
        for steps in elements:
            try:
                getattr(self.__driver, 'find_element_by_' + steps['by'])(steps['value']).click()
            except NoSuchElementException:
                pass

    def wait(self, elements):
        pass

    def goto(self, url):
        self.__driver.get(url)

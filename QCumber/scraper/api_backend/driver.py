import selenium.webdriver as se_driver


class Driver:
    raw_driver: se_driver

    def __init__(self, raw_driver: se_driver):
        self.raw_driver = raw_driver

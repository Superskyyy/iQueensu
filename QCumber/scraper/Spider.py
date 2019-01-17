from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait

from QCumber.scraper.settings.Settings import *

class Spider:
    __SCRAPER_DRIVER_DIR = None

    def __init__(self):
        self.SCRAPER_DRIVER_DIR = self.find_driver(SCRAPER_DRIVER)
        assert self.SCRAPER_DRIVER_DIR is not None, 'Driver not found!'

        option = webdriver.FirefoxOptions()

        if not (SCRAPER_LOCAL_TEST and SCRAPER_DEBUG):
            option.add_argument('-headless')
        option.add_argument('--disable-gpu')

        with webdriver.Firefox(options=option, executable_path=self.SCRAPER_DRIVER_DIR) as driver:
            driver.get('https://my.queensu.ca')

            wait = WebDriverWait(driver, 10)
            wait.until(presence_of_element_located((By.ID, 'username')))

            driver.find_element_by_id('username').send_keys(SCRAPER_USER_NAME)
            driver.find_element_by_id('password').send_keys(SCRAPER_USER_PASSWD)

            driver.find_element_by_name('_eventId_proceed').click()

            if SCRAPER_DEBUG:
                driver.get_screenshot_as_file('test.png')

            print("Logged in!")

            input()

    def find_driver_raw(self, destiny):
        print("Start searching driver under available path")
        for path in os.sys.path:
            for rel_path, dirs, files in os.walk(path):
                if destiny in files:
                    print("Driver", destiny, "found!")
                    return os.path.join(path, rel_path, destiny)
        return None

    def find_driver(self, destiny):
        config = Settings(driver_path=destiny)
        try:
            print("Start validating driver")
            config.load_from_file()
            if not os.path.exists(config.data['driver_path']):
                config.data['driver_path'] = self.find_driver_raw(destiny)
                config.save_to_file()
        except:
            config.data['driver_path'] = self.find_driver_raw(destiny)
            config.save_to_file()

        print("Driver", SCRAPER_DRIVER, "located at", config.data['driver_path'])
        return config.data['driver_path']


a = Spider()

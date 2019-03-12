import logging
import queue
from logging.handlers import QueueHandler
from logging.handlers import QueueListener
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait

from QCumber.scraper.assets.settings import *


class Spider:
    __SCRAPER_DRIVER_DIR = None

    def __init__(self):
        logger = logging.getLogger("QCumber_Scraper")
        que = queue.Queue(-1)
        queue_handler = QueueHandler(que)
        handler = logging.StreamHandler()
        listener = QueueListener(que, handler)
        logger.addHandler(queue_handler)
        formatter = logging.Formatter('%(name)s - %(asctime)s: %(message)s')
        handler.setFormatter(formatter)
        listener.start()

        # TODO: 写完websocker那块

        self.SCRAPER_DRIVER_DIR = self.find_driver(SCRAPER_DRIVER)
        assert self.SCRAPER_DRIVER_DIR is not None, 'Driver not found!'

        option = webdriver.FirefoxOptions()

        if not (SCRAPER_LOCAL_TEST and SCRAPER_DEBUG):
            option.add_argument('-headless')
        option.add_argument('--disable-gpu')

        with webdriver.Firefox(options=option, executable_path=self.SCRAPER_DRIVER_DIR) as driver:
            driver.get(
                'https://saself.ps.queensu.ca/psc/saself/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSS_BROWSE_CATLG_P.GBL')

            wait = WebDriverWait(driver, 10)
            wait.until(presence_of_element_located((By.ID, 'username')))

            driver.find_element_by_id('username').send_keys(SCRAPER_USER_NAME)
            driver.find_element_by_id('password').send_keys(SCRAPER_USER_PASSWD)

            driver.find_element_by_name('_eventId_proceed').click()

            if SCRAPER_DEBUG:
                driver.get_screenshot_as_file('test.png')

            logger.info("Logged in!")
            wait.until(presence_of_element_located((By.ID, 'DERIVED_SSS_BCC_SSS_EXPAND_ALL$97$')))
            driver.find_element_by_id("DERIVED_SSS_BCC_SSS_EXPAND_ALL$97$").click()

            i = 0
            while True:
                wait_quick = WebDriverWait(driver, 3)
                try:
                    wait_quick.until(presence_of_element_located((By.ID, "CRSE_NBR$" + str(i))))
                    item = driver.find_element_by_id("CRSE_NBR$" + str(i))
                    course_nbr = item.text
                    course_title = driver.find_element_by_id("CRSE_TITLE$" + str(i)).text
                    logger.info("course#: ", course_nbr, " course title: ", course_title)
                    item.click()
                    wait_quick.until(presence_of_element_located((By.ID, 'DERIVED_SAA_CRS_RETURN_PB$163$')))
                    driver.find_element_by_id('DERIVED_SAA_CRS_RETURN_PB$163$').click()
                except Exception:
                    break
                i = i + 1

            # instruction_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets", "process.json")
            # Process(driver).load(instruction_path).run()

    @staticmethod
    def inject_sys_path():
        print("Current OS version: " + sys.platform)
        source = os.environ["PATH"].split(";" if sys.platform.__contains__("win") else ":")
        os.sys.path.extend(source)

    def find_driver_raw(self, destiny):
        print("Start searching driver under available path")
        self.inject_sys_path()

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
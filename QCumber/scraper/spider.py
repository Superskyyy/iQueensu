import logging
import queue
import random
from logging.handlers import QueueHandler
from logging.handlers import QueueListener

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait

from QCumber.scraper.assets.settings import *


# import db_ops_for_testing


class Spider:
    __SCRAPER_DRIVER_DIR = None

    def __init__(self):

        # logging stuff
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d %H:%M',
                            filename='spider.log',
                            filemode='w')

        self.logger = logging.getLogger("QCumber_Scraper")
        self.logger.setLevel(logging.DEBUG)
        que = queue.Queue(-1)
        queue_handler = QueueHandler(que)
        handler = logging.StreamHandler()
        listener = QueueListener(que, handler)
        self.logger.addHandler(queue_handler)
        formatter = logging.Formatter('%(name)s - %(asctime)s: %(message)s')
        handler.setFormatter(formatter)
        listener.start()

        # Course_data:
        self.course_data = list()

        # TODO: 写完websocket那块

        # FIXME: inject js to remark the special courses.
        # Selenium setup
        self.SCRAPER_DRIVER_DIR = self.find_driver(SCRAPER_DRIVER)
        assert self.SCRAPER_DRIVER_DIR is not None, 'Driver not found!'

        self.option = webdriver.FirefoxOptions()

        if not (SCRAPER_LOCAL_TEST and SCRAPER_DEBUG):
            self.option.add_argument('-headless')
        self.option.add_argument('--disable-gpu')

    def solus_random_wait(self, start, stop, step):
        """
        We get a random float for spider calls
        :param start: start int
        :param step: stop int
        :param step: steps, e.g. 0.5
        :return: None
        """
        return random.randint(0, int((stop - start) / step)) * step + start

    def solus_spider(self):

        with webdriver.Firefox(options=self.option, executable_path=self.SCRAPER_DRIVER_DIR) as driver:
            driver.get(
                'https://saself.ps.queensu.ca/psc/saself/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSS_BROWSE_CATLG_P.GBL')

            wait = WebDriverWait(driver, 10)
            wait.until(presence_of_element_located((By.ID, 'username')))

            driver.find_element_by_id('username').send_keys(SCRAPER_USER_NAME)
            driver.find_element_by_id('password').send_keys(SCRAPER_USER_PASSWD)
            driver.find_element_by_name('_eventId_proceed').click()

            if SCRAPER_DEBUG:
                driver.get_screenshot_as_file('test.png')

            print("Login Successful")
            self.logger.info("Logged in!")
            wait.until(presence_of_element_located((By.ID, 'DERIVED_SSS_BCC_SSS_EXPAND_ALL$97$')))
            driver.find_element_by_id("DERIVED_SSS_BCC_SSS_EXPAND_ALL$97$").click()

            i = 0
            while True:

                # IMPORTANT NOTE > We need to
                # KEEP THE CALL TIME INTERVAL HIGH ENOUGH TO PREVENT DETECTION
                wait_quick = WebDriverWait(driver, 35, poll_frequency=self.solus_random_wait(1, 3, 0.5))
                try:
                    wait_quick.until(presence_of_element_located((By.ID, "CRSE_NBR$" + str(i))))

                    item = driver.find_element_by_id("CRSE_NBR$" + str(i))

                    course_nbr = item.text
                    if (course_nbr is "UNSP"):
                        self.logger.info("Unspecified found, ignored for now. - Sky")
                        continue
                    course_title = driver.find_element_by_id("CRSE_TITLE$" + str(i)).text
                    if ("***" in course_title):
                        self.logger.info("Multiple offering course found, ignored for now. - Sky")
                        continue
                    self.logger.info("course#: " + course_nbr + " course title: " + course_title)
                    item.click()
                    wait_quick.until(presence_of_element_located((By.ID, 'DERIVED_SAA_CRS_RETURN_PB$163$')))
                    driver.find_element_by_id('DERIVED_SAA_CRS_RETURN_PB$163$').click()

                    # save data to django model

                except Exception:  # what exception?
                    break
                i = i + 1
            # instruction_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets", "process.json")
            # Process(driver).load(instruction_path).run()

    def save_to_model(self, detail_list):
        '''
        Writes scraped data to models
        :return: None
        '''
        # 还没写完
        """
        CourseDetail_obj = CourseDetail.objects.create()
        course_obj = Course.objects.create()
        CareerPossibleValues.objects.create()
        SubjectPossibleValues.objects.create()
        CampusPossibleValues.objects.create()
        GradingPossibleValues.objects.create()
        AcademicGroupPossibleValues.objects.create()
        AcademicOrganizationPossibleValues.objects.create()
        Components.objects.create()
        EnrollmentInformation.objects.create()
        """

    @staticmethod
    def inject_sys_path():
        print("Current OS version: " + sys.platform)
        source = os.environ["PATH"].split(";" if sys.platform.__contains__("win") else ":")
        os.sys.path.extend(source)

    def find_driver_raw(self, destiny):
        print("Start searching driver under available path")
        self.inject_sys_path()

        for path in os.sys.path:
            print(path)
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

    def scraper_start(self):
        my_spider = Spider()
        my_spider.solus_spider()


if __name__ == '__main__':
    my_spider = Spider()
    my_spider.scraper_start()

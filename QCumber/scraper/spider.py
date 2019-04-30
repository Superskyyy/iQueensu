import logging
import queue
import random
import time
from logging.handlers import QueueHandler
from logging.handlers import QueueListener

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait

from QCumber.scraper.assets.models import *
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
        :return: float
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

            # first get a list of subject full names
            counter = 0
            subject_full_names = []

            while True:
                try:
                    subject_full_name = driver.find_element_by_id(
                        "DERIVED_SSS_BCC_GROUP_BOX_1$147$$" + str(counter)).text
                    subject_full_names.append(subject_full_name)
                except:
                    break
                counter += 1
            print(subject_full_names)
            i = 0
            while True:
                detail_dict = {}
                # IMPORTANT NOTE > We need to
                # KEEP THE CALL TIME INTERVAL HIGH ENOUGH TO PREVENT DETECTION
                wait_quick = WebDriverWait(driver, 35, poll_frequency=self.solus_random_wait(1, 3, 0.5))
                # try:
                wait_quick.until(presence_of_element_located((By.ID, "CRSE_NBR$" + str(i))))

                item = driver.find_element_by_id("CRSE_NBR$" + str(i))

                course_nbr = item.text
                if ("UNS" in course_nbr):
                    self.logger.info("Unspecified found, ignored for now. - Sky")
                    i += 1
                    continue
                course_title = driver.find_element_by_id("CRSE_TITLE$" + str(i)).text
                if ("***" in course_title):
                    self.logger.info("Multiple offering course found, ignored for now. - Sky")
                    i += 1
                    continue

                self.logger.info("course#: " + course_nbr + " course title: " + course_title)

                # FIXME: this subject needs special attention




                # click into the course
                # we wait few seconds here to minimize chances of getting caught
                time.sleep(self.solus_random_wait(2, 5, 0.5))
                item.click()

                # data prepare
                wait_quick.until(presence_of_element_located((By.ID, 'SSR_CRSE_OFF_VW_ACAD_CAREER$0')))
                # get subject

                detail_dict["subject_code"] = driver.find_element_by_id("DERIVED_CRSECAT_DESCR200").text[:4]
                for names in subject_full_names:
                    if detail_dict["subject_code"] in names:
                        detail_dict["subject_name"] = names[7:]

                detail_dict["career"] = driver.find_element_by_id("SSR_CRSE_OFF_VW_ACAD_CAREER$0").text
                detail_dict["units"] = driver.find_element_by_id("DERIVED_CRSECAT_UNITS_RANGE$0").text
                detail_dict["grading"] = driver.find_element_by_id("SSR_CRSE_OFF_VW_GRADING_BASIS$0").text
                detail_dict["components_description"] = driver.find_element_by_id("DERIVED_CRSECAT_DESCR$0").text
                detail_dict["campus"] = driver.find_element_by_id("CAMPUS_TBL_DESCR$0").text
                detail_dict["academic_group"] = driver.find_element_by_id("ACAD_GROUP_TBL_DESCR$0").text
                detail_dict["academic_org"] = driver.find_element_by_id("ACAD_ORG_TBL_DESCR$0").text
                detail_dict["enroll_add_consent"] = driver.find_element_by_id("SSR_CRSE_OFF_VW_CONSENT$0").text
                detail_dict["enroll_drop_consent"] = driver.find_element_by_id(
                    "SSR_CRSE_OFF_VW_SSR_DROP_CONSENT$0").text
                detail_dict["course_description"] = driver.find_element_by_id("SSR_CRSE_OFF_VW_DESCRLONG$0").text
                detail_dict["course_title"] = course_title
                detail_dict["course_number"] = course_nbr

                # this line seems useless
                wait_quick.until(presence_of_element_located((By.ID, 'DERIVED_SAA_CRS_RETURN_PB$163$')))
                driver.find_element_by_id('DERIVED_SAA_CRS_RETURN_PB$163$').click()

                # save data to django model
                # print(detail_dict.values())
                self.save_to_model(detail_dict)

                # except Exception:  # what exception?
                # print(Exception)
                i = i + 1
            # instruction_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets", "process.json")
            # Process(driver).load(instruction_path).run()

    def save_to_model(self, detail_dict):
        """
         Writes scraped data to django ORM models
                :return: None

        Details Example:

        detail_dict = {"career": "Graduate",
                       "units": "3.00",
                       "grading": "Graded",
                       "components_description": "Seminar",
                       "campus": "Main",
                       "academic_group": "Faculty of Health Sciences",
                       "academic_org": "REH (not department specific)",
                       "enroll_add_consent": "Department Consent Required",
                       "enroll_drop_consent":"Department Consent Required",
                       "course_description": "This cource simply blows you mind",
                       "course_title": "Fundamental Computing Theroy",
                       "course_number": "998",
                       "subject_code": "CISC",
                       "subject_name": "Computer Infomation and Science"
                       }

        """

        course_object = Course(details=CourseDetail.objects.create(
            career=CareerPossibleValues.objects.create(career=detail_dict["career"]),
            units=detail_dict["units"],
            grading_basis=GradingPossibleValues.objects.create(grading=detail_dict["grading"]),
            course_components=Components.objects.create(description=detail_dict["components_description"]),
            campus=CampusPossibleValues.objects.create(campus=detail_dict["campus"]),
            academic_group=AcademicGroupPossibleValues.objects.create(academic_group=detail_dict["academic_group"]),
            academic_organization=AcademicOrganizationPossibleValues.objects.create(
                academic_organization=detail_dict["academic_org"]),
            enrollment=EnrollmentInformation.objects.create(enroll_add_consent=detail_dict["enroll_add_consent"],
                                                            enroll_drop_consent=detail_dict["enroll_drop_consent"]),
            description=CourseDescription.objects.create(description=detail_dict["course_description"]), ),
            name=detail_dict["course_title"],
            number=detail_dict["course_number"],
            subject=SubjectPossibleValues.objects.create(code=detail_dict['subject_code'],
                                                         name=detail_dict["subject_name"])
        )
        course_object.save()

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
    # my_spider.scraper_start()
    my_spider.save_to_model({})

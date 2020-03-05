"""
This is a selenium spider that crawls all the course catalog data
from our SOLUS system.
"""
import logging
import os
import queue
import random
import re
import sys
import time
from logging.handlers import QueueHandler
from logging.handlers import QueueListener

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait

from QCumber.scraper.assets.models import (
    Course,
    CourseDetail,
    AcademicGroupPossibleValues,
    AcademicOrganizationPossibleValues,
    CampusPossibleValues,
    CareerPossibleValues,
    Components,
    CourseDescription,
    EnrollmentInformation,
    GradingPossibleValues,
    LearningHours,
    SubjectPossibleValues,
)

try:
    from QCumber.scraper.assets.settings import (
        SCRAPER_USER_NAME,
        SCRAPER_USER_PASSWD,
        SCRAPER_DEBUG,
        SCRAPER_LOCAL_TEST,
    )
except ModuleNotFoundError as error:
    print(
        """
        Please copy QCumber/scraper/assets/settings_example.py as settings.py in the same folder,
        and edit the settings as instructed in the file.
        #Notice, settings.py is ignored by .gitignore file, everything in that file WILL BE LOST in CVS.
    """
    )
    # sys.exit(1)  # force to stop

    # make PyCharm feel happy even if there's no settings.py
    # Theoretically, Following line should be never executed.


# import db_ops_for_testing


class Spider:
    """
    Main spider class.
    """

    __SCRAPER_DRIVER_DIR = None

    def __init__(self):

        ######for testing flush db before doing

        def flush_db():
            Course.objects.all().delete()
            CourseDetail.objects.all().delete()
            AcademicGroupPossibleValues.objects.all().delete()
            AcademicOrganizationPossibleValues.objects.all().delete()
            CampusPossibleValues.objects.all().delete()
            CareerPossibleValues.objects.all().delete()
            Components.objects.all().delete()
            CourseDescription.objects.all().delete()
            EnrollmentInformation.objects.all().delete()
            GradingPossibleValues.objects.all().delete()
            SubjectPossibleValues.objects.all().delete()

        flush_db()

        # logging stuff
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
            datefmt="%m-%d %H:%M",
            filename="spider.log",
            filemode="w",
        )

        self.logger = logging.getLogger("QCumber_Scraper")
        self.logger.setLevel(logging.DEBUG)
        que = queue.Queue(-1)
        queue_handler = QueueHandler(que)
        handler = logging.StreamHandler()
        listener = QueueListener(que, handler)
        self.logger.addHandler(queue_handler)
        formatter = logging.Formatter("%(name)s - %(asctime)s: %(message)s")
        handler.setFormatter(formatter)
        listener.start()

        # Course_data:
        self.course_data = list()

        # TODO: 写完websocket那块

        # FIXME: inject js to remark the special courses.

        self.option = webdriver.FirefoxOptions()

        if not SCRAPER_LOCAL_TEST:
            self.option.add_argument("-headless")
        self.option.add_argument("--disable-gpu")

    @staticmethod
    def solus_random_wait(start: int, stop: int, step: float):
        """
        We get a random float for spider calls
        :param start: start int
        :param stop: stop int
        :param step: steps, e.g. 0.5
        :return: float
        """
        return random.randint(0, int((stop - start) / step)) * step + start

    def solus_spider(self):  # pylint: disable=too-many-statements
        """
        Spider main
        :return: None
        """
        time.sleep(3)

        with webdriver.Remote(
                options=self.option,
                command_executor="http://chrome:4444/wd/hub",
                desired_capabilities=DesiredCapabilities.CHROME,
        ) as driver:
            driver.get(
                "https://saself.ps.queensu.ca/psc/saself/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSS_BROWSE_CATLG_P.GBL"
            )

            wait = WebDriverWait(driver, 15)
            wait.until(presence_of_element_located((By.ID, "username")))

            driver.find_element_by_id("username").send_keys(SCRAPER_USER_NAME)
            driver.find_element_by_id("password").send_keys(SCRAPER_USER_PASSWD)
            driver.find_element_by_name("_eventId_proceed").click()

            time.sleep(5)
            wait.until(
                presence_of_element_located(
                    (By.ID, "DERIVED_SSS_BCC_SSS_EXPAND_ALL$97$")
                )
            )
            print("Login Successful")

            self.logger.info("Logged in!")
            driver.find_element_by_id("DERIVED_SSS_BCC_SSS_EXPAND_ALL$97$").click()

            # first get a list of subject full names
            counter = 0
            subject_full_names = []

            while True:
                try:
                    subject_full_name = driver.find_element_by_id(
                        "DERIVED_SSS_BCC_GROUP_BOX_1$147$$" + str(counter)
                    ).text
                    subject_full_names.append(subject_full_name)
                except exceptions.NoSuchElementException:
                    break
                counter += 1

            print(subject_full_names)
            course_nbr_id = 0

            while True:
                detail_dict = {}
                # IMPORTANT NOTE > We need to
                # KEEP THE CALL TIME INTERVAL HIGH ENOUGH TO PREVENT DETECTION
                wait_quick = WebDriverWait(
                    driver, 35, poll_frequency=self.solus_random_wait(1, 3, 0.5)
                )
                # try:
                wait_quick.until(
                    presence_of_element_located(
                        (By.ID, "CRSE_NBR$" + str(course_nbr_id))
                    )
                )

                item = driver.find_element_by_id("CRSE_NBR$" + str(course_nbr_id))
                course_nbr = item.text

                if "UNS" in course_nbr:
                    self.logger.info("Unspecified found, ignored for now. - Sky")
                    course_nbr_id += 1
                    continue
                course_title = driver.find_element_by_id(
                    "CRSE_TITLE$" + str(course_nbr_id)
                ).text
                if "***" in course_title:
                    self.logger.info(
                        "Multiple offering course found, ignored for now. - Sky"
                    )
                    course_nbr_id += 1
                    continue

                self.logger.info(
                    "course#: " + course_nbr + " course title: " + course_title
                )

                # FIXME: this subject needs special attention

                # click into the course
                # we wait few seconds here to minimize chances of getting caught
                time.sleep(self.solus_random_wait(2, 5, 0.5))
                item.click()

                # data prepare

                # FIXME SPIDER DIED at this line, investigation needed. after web_1
                # 'course_title': 'Theatre Administration', 'course_number': '820'}
                #  | QCumber_Scraper - 2020-02-02 17:45:24,481: course#: 101 course title: Astronomy I: Solar System
                wait_quick.until(
                    presence_of_element_located(
                        (By.ID, "SSR_CRSE_OFF_VW_ACAD_CAREER$0")
                    )
                )

                detail_dict["subject_code"] = driver.find_element_by_id(
                    "DERIVED_CRSECAT_DESCR200"
                ).text[:4]
                for names in subject_full_names:
                    if detail_dict["subject_code"] in names:
                        detail_dict["subject_name"] = names[7:]
                try:
                    detail_dict["career"] = driver.find_element_by_id(
                        "SSR_CRSE_OFF_VW_ACAD_CAREER$0"
                    ).text
                except exceptions.NoSuchElementException:
                    detail_dict["career"] = "Not Specified"

                try:
                    detail_dict["units"] = driver.find_element_by_id(
                        "DERIVED_CRSECAT_UNITS_RANGE$0"
                    ).text
                except exceptions.NoSuchElementException:
                    detail_dict["units"] = "Not Specified"

                try:
                    detail_dict["grading"] = driver.find_element_by_id(
                        "SSR_CRSE_OFF_VW_GRADING_BASIS$0"
                    ).text
                except exceptions.NoSuchElementException:
                    detail_dict["grading"] = "Not Specified"

                try:
                    detail_dict["components_description"] = driver.find_element_by_id(
                        "DERIVED_CRSECAT_DESCR$0"
                    ).text
                except exceptions.NoSuchElementException:
                    detail_dict["components_description"] = "Not Specified"

                try:
                    detail_dict["campus"] = driver.find_element_by_id(
                        "CAMPUS_TBL_DESCR$0"
                    ).text
                except exceptions.NoSuchElementException:
                    detail_dict["campus"] = "Not Specified"

                try:
                    detail_dict["academic_group"] = driver.find_element_by_id(
                        "ACAD_GROUP_TBL_DESCR$0"
                    ).text
                except exceptions.NoSuchElementException:
                    detail_dict["academic_group"] = "Not Specified"

                try:
                    detail_dict["academic_org"] = driver.find_element_by_id(
                        "ACAD_ORG_TBL_DESCR$0"
                    ).text
                except exceptions.NoSuchElementException:
                    detail_dict["academic_org"] = "Not Specified"

                try:
                    detail_dict["enroll_add_consent"] = driver.find_element_by_id(
                        "SSR_CRSE_OFF_VW_CONSENT$0"
                    ).text
                except exceptions.NoSuchElementException:
                    detail_dict["enroll_add_consent"] = "Not Specified"

                try:
                    detail_dict["enroll_drop_consent"] = driver.find_element_by_id(
                        "SSR_CRSE_OFF_VW_SSR_DROP_CONSENT$0"
                    ).text
                except exceptions.NoSuchElementException:
                    detail_dict["enroll_drop_consent"] = "Not Specified"

                # FIXME add enrollment prerequisites
                try:
                    # Find learning hours among course descriptions:
                    description_raw = driver.find_element_by_id(
                        "SSR_CRSE_OFF_VW_DESCRLONG$0"
                    ).text
                except exceptions.NoSuchElementException:
                    description_raw = "Not Specified"
                learning_hours_regex = re.compile(
                    r"LEARNING HOURS(\s*)([0-9]*)(\s*)\((.*)\)"
                )
                learning_hours_regex_queried = re.search(
                    learning_hours_regex, description_raw
                )

                if not learning_hours_regex_queried:
                    detail_dict["learning_hours"] = "-1"

                    detail_dict["course_description"] = description_raw
                else:
                    detail_dict["course_description"] = description_raw.replace(learning_hours_regex_queried.group(),
                                                                                "")
                    fixed = learning_hours_regex_queried.group().replace(
                        "LEARNING HOURS ", ""
                    )
                    detail_dict["learning_hours"] = fixed

                detail_dict["course_title"] = course_title
                detail_dict["course_number"] = course_nbr

                # this line seems useless
                wait_quick.until(
                    presence_of_element_located(
                        (By.ID, "DERIVED_SAA_CRS_RETURN_PB$163$")
                    )
                )
                driver.find_element_by_id("DERIVED_SAA_CRS_RETURN_PB$163$").click()

                # save data to django model
                # print(detail_dict.values())
                self.save_to_model(detail_dict)

                course_nbr_id = course_nbr_id + 1

    @staticmethod
    def save_to_model(detail_dict):
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
                       "learning_hours": "azzzzz"
                       "course_description": "This course simply blows you mind",
                       "course_title": "Fundamental Computing Theory",
                       "course_number": "998",
                       "subject_code": "CISC",
                       "subject_name": "Computer Information and Science"
                       }

        """
        print(detail_dict)
        # get_or_create returns tuple (object-bool)
        course_object = Course(
            details=CourseDetail.objects.create(
                career=CareerPossibleValues.objects.get_or_create(
                    career=detail_dict["career"]
                )[0],
                units=detail_dict["units"],
                grading_basis=GradingPossibleValues.objects.get_or_create(
                    grading=detail_dict["grading"]
                )[0],
                course_components=Components.objects.get_or_create(
                    description=detail_dict["components_description"]
                )[0],
                campus=CampusPossibleValues.objects.get_or_create(
                    campus=detail_dict["campus"]
                )[0],
                academic_group=AcademicGroupPossibleValues.objects.get_or_create(
                    academic_group=detail_dict["academic_group"]
                )[0],
                academic_organization=AcademicOrganizationPossibleValues.objects.get_or_create(
                    academic_organization=detail_dict["academic_org"]
                )[
                    0
                ],
                enrollment=EnrollmentInformation.objects.get_or_create(
                    enroll_add_consent=detail_dict["enroll_add_consent"],
                    enroll_drop_consent=detail_dict["enroll_drop_consent"],
                )[0],
                learning_hours=LearningHours.objects.get_or_create(
                    learning_hours=detail_dict["learning_hours"]
                )[0],
                description=CourseDescription.objects.get_or_create(
                    description=detail_dict["course_description"]
                )[0],
            ),
            name=detail_dict["course_title"],
            number=detail_dict["course_number"],
            subject=SubjectPossibleValues.objects.get_or_create(
                code=detail_dict["subject_code"], name=detail_dict["subject_name"]
            )[0],
        )
        course_object.save()

    @staticmethod
    def inject_sys_path():
        """
        Inject sys path
        :return:
        """
        print("Current OS version: " + sys.platform)
        source = os.environ["PATH"].split(
            ";" if sys.platform.__contains__("win") else ":"
        )
        os.sys.path.extend(source)

    @staticmethod
    def scraper_start():
        """
        A function used in admin panel - admin.py
        :return:
        """
        new_spider = Spider()
        new_spider.solus_spider()


if __name__ == "__main__":
    my_spider = Spider()
    # my_spider.scraper_start()
    my_spider.save_to_model({})

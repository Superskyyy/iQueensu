"""
This is a panel for the admin page of QCumber applications
"""
import json

from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, re_path

from QCumber.scraper.assets.models import CourseDetail, Course, GradeDistribution
from QCumber.scraper.spider import Spider
from QCumber.scraper.spider_grade import SpiderGrade


@admin.register(CourseDetail)
class CourseDetailAdmin(admin.ModelAdmin):
    """
    The Admin page for CourseDetail
    """

    list_display = (
        "career",
        "units",
        "grading_basis",
        "course_components",
        "campus",
        "academic_group",
        "academic_organization",
        "enrollment",
        "learning_hours",
        "description",
    )
    list_filter = ("units", "career", "campus")

@admin.register(GradeDistribution)
class GradeDistributionAdmin(admin.ModelAdmin):
    """The Admin page for GradeDistribution"""
    # list_display = ("gradeDistribution")
    change_list_template = "spider_grade.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            url("grade-scraper-start/", self.set_scraper_grade_start),
        ]
        return my_urls + urls

    def set_scraper_grade_start(self, request):
        """
        Simply invokes the spider class
        :param request: request is a request
        :return: Http Redirect
        """
        # try:
        self.message_user(request, "Scraper start triggered")
        SpiderGrade.main()
        # except:
        print("Scraper failed")

        self.message_user(request, "Scraper has completed")

        return HttpResponseRedirect("../")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    The Admin page for Courses
    """

    list_display = ("subject", "number", "name", "details")
    list_filter = ("number",)
    change_list_template = "spider_operations.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("spider-username/<slug:username>/", self.set_credentials),
            path("spider-password/<slug:password>/", self.set_credentials),
            re_path(
                r"spider-credentials/(?P<credentials>(.*);;;(.*))/",
                self.set_credentials,
            ),
            url("solus-course-scraper-start/", self.set_scraper_start),
            url("solus-course-scraper-terminate/", self.set_scraper_terminate),
        ]
        return my_urls + urls

    def set_credentials(self, request, credentials=""):
        """
        get credentials from the requests and set them into env vars / json
        :param request: Request is from the get_urls path()
        :return:
        """

        def set_credentials(username: str, password: str):
            credentials_json = {"username": username, "password": password}
            try:
                with open(
                        "QCumber/scraper/assets/spider_credentials.json", "w"
                ) as credentials_out:
                    json.dump(credentials_json, credentials_out)
                    print("success a ")
            except IOError:
                print(IOError)
                return 1
            else:
                return 0

        if credentials:
            credentials = credentials.split(";;;")
            username = credentials[0]
            password = credentials[1]
            print(f"Username is {username} Password is {password}")

            if set_credentials(username=username, password=password) == 0:
                self.message_user(request, "Credentials set!")

                return HttpResponseRedirect("/admin/QCumber/course/")

    def set_scraper_start(self, request):
        """
        Simply invokes the spider class
        :param request: request is a request
        :return: Http Redirect
        """
        # try:
        self.message_user(request, "Scraper start triggered")

        Spider().scraper_start()
        # except:
        print("Scraper failed")

        self.message_user(request, "Scraper has completed")

        return HttpResponseRedirect("../")

    def set_scraper_terminate(self, request):
        """
        terminate a spider scrape that is "somehow"
        not acting right not implemented
        :param request:
        :return:
        """
        self.message_user(request, "Scraper terminated - stub message")
        return HttpResponseRedirect("../")

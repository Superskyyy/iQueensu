from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponseRedirect

from QCumber.scraper.assets.models import *
from QCumber.scraper.spider import Spider


# Register your models here.
# admin.site.register(CareerPossibleValues)
# admin.site.register(SubjectPossibleValues)
# admin.site.register(CampusPossibleValues)
# admin.site.register(GradingPossibleValues)
# admin.site.register(AcademicGroupPossibleValues)
# admin.site.register(AcademicOrganizationPossibleValues)
# admin.site.register(Components)
# admin.site.register(EnrollmentInformation)
# admin.site.register(CourseDescription)
# admin.site.register(CourseDetail)
# admin.site.register(Course)

@admin.register(Course, CourseDetail)
class HeroAdmin(admin.ModelAdmin):
    change_list_template = "start_scraper.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            url('solus-course-scraper-start/', self.set_scraper_start),
            url('solus-course-scraper-terminate/', self.set_scraper_terminate),
        ]
        return my_urls + urls

    def set_scraper_start(self, request):
        try:
            self.message_user(request, "Scraper start triggered")

            new_scrape = Spider().save_to_model({})
        except:
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

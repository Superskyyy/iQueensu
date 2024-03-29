"""
This module defines the router
QCumber/urls.py
"""
from django.urls import path, include
from rest_framework import routers

from QCumber.api import views

router = routers.DefaultRouter()
router.register(r"courses", views.CourseViewSet)
router.register(r"courseDetails", views.CourseDetailViewSet)

router.register(r"courseRatings", views.CourseRatingViewSet)


router.register(r"gradeDistribution", views.GradeDistributionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [path("api/v1/qcumber/", include(router.urls))]

# path('search/<slug:keyword>',views.course_search)
#    path('apis/', include('rest_framework.urls', namespace='rest_framework'))

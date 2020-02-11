# Qusers/urls.py
from django.urls import include, path
from rest_framework import routers
from QUser import views

router = routers.DefaultRouter()
router.register(r'users', views.QUserListView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.QUserListView.as_view()),
]
'''
# Qusers/urls.py
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.QUserListView.as_view()),
    ]

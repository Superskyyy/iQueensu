# QCumber/urls.py
from django.urls import path

from QCumber.api import views

urlpatterns = [
    path('api/v1/qcumber/', views.QCumberListCreate.as_view()),
]

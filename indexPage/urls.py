from django.urls import path
from catalog import views

# test for index page

urlpatterns = [
    path('', views.index, name='index'),
]

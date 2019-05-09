from django.urls import path

from . import views

# test for index page
app_name = 'indexPage'

'''
urlpatterns = [
    path('', views.index, name='index'),
    path('qhome', views.qhome, name='qhome'),
]
'''
urlpatterns = [
    path('bbs', views.bbs)
]

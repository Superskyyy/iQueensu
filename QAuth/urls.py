# QAuth/urls.py

"""
added a endpoint to list all users
added path to rest-auth
"""
from django.urls import include, path

urlpatterns = [
    path('users/', include('QUser.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]

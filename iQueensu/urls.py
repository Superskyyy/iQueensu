"""iQueensu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

# from rest_framework_jwt_sso import views
#    path('',views.hw),
urlpatterns = [
    path("admin/", admin.site.urls),
    path("qcumber/", include("QCumber.api.urls")),
]
#    path('qapi_v0/', include('QAPI.urls')),
#    path('qauth_v0/', include('QAuth.urls')),

# Qcumber api
urlpatterns += [path("", include("QCumber.api.urls"))]

# Add URL maps to redirect the base URL to our application

urlpatterns += [path("", RedirectView.as_view(url="/admin"))]
# indexPage/bbs

#djoser auth
urlpatterns += [
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt'))
]

# Use static() to add url mapping to serve static files during development (only)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

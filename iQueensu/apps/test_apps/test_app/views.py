from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.templatetags.staticfiles import static

# Create your views here.

def index(request):
    return render(request, "index.html")

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
# Create your views here.

def index(request):
    if (request.GET.get('dev') == '2'):
        return render(request,'indexPage/index.html', {'dev': { 'test': True, 'api': settings.REST_API_ADDRESS}})
    else:
        return HttpResponse("Coming soon", status=418)

def qhome(request):
    return render(request,'indexPage/qhome/qhome.html')
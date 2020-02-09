# noinspection PyPackageRequirements
import json

from django.conf import settings
from django.http import HttpResponse
# for redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

def index(request):
    if request.GET.get('dev') == '2':
        return render(request, 'indexPage/index.html', {'dev': {'test': True, 'api': settings.REST_API_ADDRESS}})
    else:
        return HttpResponse("Coming soon", status=418)


def qhome(request):
    jsondata = json.dumps({
        'api_addr': "/" + settings.REST_API_ADDRESS
    })
    print(jsondata)
    return render(request, 'indexPage/qhome/qhome.html', {'qhome': {'data': jsondata}})


def bbs(request):
    return HttpResponseRedirect("https://bbs.iqueensu.ca")

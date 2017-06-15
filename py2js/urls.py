"""py2js URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from pycow import translate_string
from django.views.decorators.csrf import csrf_exempt
import base64

@csrf_exempt
def py2js(request):
    try:
        return HttpResponse(translate_string(base64.decodestring(request.POST["q"])))
    except Exception, e:
        return HttpResponse("Error while compiling:" + e.message)
    
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^py2js$', py2js),
]

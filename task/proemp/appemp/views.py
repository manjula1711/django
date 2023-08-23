

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import db



def homepage(request):
    template=loader.get_template("att.html")
    return HttpResponse(template.render())
def loginpage(request):
    template=loader.get_template("login.html")
    return HttpResponse(template.render({},request))
def addmembers(request):
     template=loader.get_template("addmembers.html")
     return HttpResponse(template.render({},request))
     
def check(request):
    template=loader.get_template("check.html")
    return HttpResponse(template.render({},request))
def dashboard(request):
    template=loader.get_template("dashboard.html")
    return HttpResponse(template.render({},request))


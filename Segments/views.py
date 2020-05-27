from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def IT(request):
    return render(request,'It.html')


def language(request):
    return render(request,'Lang.html')


def Scholar(request):
    return render(request,'Scholars.html')


def gov(request):
    return render(request,'Govornor.html')
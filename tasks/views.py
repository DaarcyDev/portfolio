from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from .models import Skill, About, Project, Blog 
# Create your views here.

def index(request):
    about = About.objects.all()
    return render ( request, 'index.html', {
        "abouts":about
    })


def DaarcyDevAdmin(request):
    return render ( request, 'adminDaarcyDev.html')

    
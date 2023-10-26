from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from .models import Skill, About, Project, SkillsImages
# Create your views here.

def index(request):
    about = About.objects.all()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    skillsImage = SkillsImages.objects.all()
    return render ( request, 'index.html', {
        "abouts":about,
        "projects":projects,
        "skills":skills,
        "skillsImages":skillsImage
    })


def DaarcyDevAdmin(request):
    return render ( request, 'adminDaarcyDev.html')

    
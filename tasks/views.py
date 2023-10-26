from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from .models import Skill, About, Project, SkillsImages, ProjectImages
# Create your views here.

def index(request):
    about = About.objects.all()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    skillsImage = SkillsImages.objects.all()
    projectImages = ProjectImages.objects.all()
    return render ( request, 'index.html', {
        "abouts":about,
        "projects":projects,
        "skills":skills,
        "skillsImages":skillsImage,
        "projectImages": projectImages
    })


def DaarcyDevAdmin(request):
    return render ( request, 'adminDaarcyDev.html')

    
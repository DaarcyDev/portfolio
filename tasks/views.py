from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from .models import Skill, About, Project, SkillsImages, ProjectImages, BlogCategory, BlogFile
# Create your views here.

def index(request):
    about = About.objects.all()
    skills = Skill.objects.all()
    skillsImage = SkillsImages.objects.all()
    projects = Project.objects.all()
    projectImages = ProjectImages.objects.all()
    blogCategory = BlogCategory.objects.all()
    blogFile = BlogFile.objects.all()
    return render ( request, 'index.html', {
        "abouts":about,
        "projects":projects,
        "skills":skills,
        "skillsImages":skillsImage,
        "projectImages": projectImages,
        "blogCategories": blogCategory,
        "blogFiles": blogFile
    })


def DaarcyDevAdmin(request):
    return render ( request, 'adminDaarcyDev.html')

    
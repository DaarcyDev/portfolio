from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Skill, About, Project, SkillsImages, ProjectImages, BlogCategory, BlogFile, Contact
# Create your views here.

def index(request):
    about = About.objects.all()
    skills = Skill.objects.all()
    skillsImage = SkillsImages.objects.all()
    projects = Project.objects.all()
    projectImages = ProjectImages.objects.all()
    blogCategory = BlogCategory.objects.all()
    blogFile = BlogFile.objects.all()
    contact = Contact.objects.all()
    return render ( request, 'index.html', {
        "abouts":about,
        "projects":projects,
        "skills":skills,
        "skillsImages":skillsImage,
        "projectImages": projectImages,
        "blogCategories": blogCategory,
        "blogFiles": blogFile,
        "contacts": contact
    })

def DaarcyDevAdmin(request):
    
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'adminDaarcyDev.html',
                      {
                          'form': form
                          })
    
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('crud') 

    

@login_required
def crud(request):
    return render ( request, 'crud.html')


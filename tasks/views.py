from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Skill, About, Project, SkillsImages, ProjectImages, BlogCategory, BlogFile, Contact
from .forms import AboutForm, ProjectForm, ProjectImageForm

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
    return render(request, 'crud.html')


@login_required
def crudAbout(request):
    if(request.method == "GET"):
        return render(request, 'aboutCrud.html', {
            'formAbout': AboutForm,
        })
    else:
        try:
            formAbout = AboutForm(request.POST, request.FILES)
            new_product = formAbout.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return redirect("admin")
        except:
            return render(request, 'aboutCrud.html',{
            'formAbout': AboutForm,
            'error': 'please provide valide data'
        })

@login_required
def crudProject(request):
    projects = Project.objects.all()
    projectImages = ProjectImages.objects.all()
    return render ( request, 'projectCrud.html', {
        "projects":projects,
        "projectImages": projectImages,
    })


@login_required
def crudProjectCreate(request):
    if(request.method == "GET"):
        return render(request, 'projectCrudCreate.html', {
            'projectForm': ProjectForm,
            'projectImageForm': ProjectImageForm,
        })
    else:
        try:
            formProject = ProjectForm(request.POST, request.FILES)
            new_product = formProject.save(commit=False)
            new_product.user = request.user
            new_product.save()

            projectWebsiteImages = request.FILES.getlist('projectWebsiteImages')
            projectWebsiteTools = request.FILES.getlist('projectWebsiteTools')

            for image in projectWebsiteImages:
                new_image = ProjectImages(projectWebsiteImages=image)
                new_image.project = new_product
                new_image.save()

            for image in projectWebsiteTools:
                new_image = ProjectImages(projectWebsiteTools=image)
                new_image.project = new_product
                new_image.save()

            return redirect("admin")
        except:
            return render(request, 'projectCrudCreate.html',{
                'projectForm': ProjectForm,
                'projectImageForm': ProjectImageForm,
                'error': 'please provide valide data'
            })

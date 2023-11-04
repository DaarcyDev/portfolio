from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Skill, About, Project, SkillsImages, ProjectImages, BlogCategory, BlogFile, Contact
from .forms import AboutForm, ProjectForm, ProjectImageForm, SkillsForm, SkillsImageForm
from django.shortcuts import get_object_or_404



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
    about = About.objects.all()
    return render ( request, 'aboutCrud.html', {
        "abouts":about,
    })

@login_required
def crudAboutCreate(request):
    if(request.method == "GET"):
        return render(request, 'aboutCrudCreate.html', {
            'formAbout': AboutForm,
        })
    else:
        try:
            formAbout = AboutForm(request.POST, request.FILES)
            new_product = formAbout.save(commit=False)
            new_product.save()
            return redirect("crudAbout")
        except:
            return render(request, 'aboutCrudCreate.html',{
            'formAbout': AboutForm,
            'error': 'please provide valide data'
        })

@login_required
def crudAboutUpdate(request, pk):
    about = About.objects.get(pk=pk)
    if request.method == "GET":
        formAbout = AboutForm(instance=about)

    else:
        try:
            formAbout = AboutForm(request.POST, request.FILES, instance=about)
            new_product = formAbout.save(commit=False)
            new_product.save()
            return redirect("crudAbout")
        except:
            return render(request, 'aboutCrudUpdate.html',{
                'formAbout': formAbout,
                'error': 'please provide valide data'
            })
    return render(request, 'aboutCrudUpdate.html', {
        'formAbout': formAbout,
    })

@login_required
def crudAboutDelete(request, pk):
    about = About.objects.get(pk=pk)
    about.delete()

    return redirect("crudAbout")

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

            return redirect("crudProject")
        except:
            return render(request, 'projectCrudCreate.html',{
                'projectForm': ProjectForm,
                'projectImageForm': ProjectImageForm,
                'error': 'please provide valide data'
            })

@login_required
def crudProjectUpdate(request, pk):
    project = Project.objects.get(pk=pk)

    if request.method == "GET":
        projectForm = ProjectForm(instance=project)
        projectImageForm = ProjectImageForm(instance=project)
    else:
        projectForm = ProjectForm(request.POST, request.FILES, instance=project)
        if projectForm.is_valid():
            new_product = projectForm.save(commit=False)
            new_product.save()

            projectWebsiteImages = request.FILES.getlist('projectWebsiteImages')
            projectWebsiteTools = request.FILES.getlist('projectWebsiteTools')
            
            if projectWebsiteImages:
                images = project.images.filter(project_id=project, projectWebsiteImages__isnull=False).values('projectWebsiteImages')
                filtered_images = images.exclude(projectWebsiteImages="")
                image_ids = filtered_images.values_list('id', flat=True)

                if image_ids:
                    for value1 in image_ids:

                        images_to_delete = ProjectImages.objects.filter(id=value1)
                        images_to_delete.delete()

                    if projectWebsiteImages:
                        for image in projectWebsiteImages:
                            new_image = ProjectImages(projectWebsiteImages=image)
                            new_image.project = new_product
                            new_image.save()
                else:
                    if projectWebsiteImages:
                        for image in projectWebsiteImages:
                            new_image = ProjectImages(projectWebsiteImages=image)
                            new_image.project = new_product
                            new_image.save()
                        
            if projectWebsiteTools:
                images = project.images.filter(project_id=project, projectWebsiteTools__isnull=False).values('projectWebsiteTools')
                filtered_images = images.exclude(projectWebsiteTools="")
                image_ids = filtered_images.values_list('id', flat=True)

                if image_ids:
                    for value1 in image_ids:

                        images_to_delete = ProjectImages.objects.filter(id=value1)
                        images_to_delete.delete()

                    if projectWebsiteTools:
                        for image in projectWebsiteTools:
                            new_image = ProjectImages(projectWebsiteTools=image)
                            new_image.project = new_product
                            new_image.save()
                else:
                    if projectWebsiteTools:
                        for image in projectWebsiteTools:
                            new_image = ProjectImages(projectWebsiteTools=image)
                            new_image.project = new_product
                            new_image.save()
            
            
            return redirect("crudProject")
    
    return render(request, 'projectCrudUpdate.html', {
        'projectForm': projectForm,
        'projectImageForm': projectImageForm,
    })

@login_required
def crudProjectDelete(request, pk):
    project = Project.objects.get(pk=pk)
    project.delete()

    return redirect("crudProject")

@login_required
def crudSkill(request):
    skills = Skill.objects.all()
    skillsImages = SkillsImages.objects.all()
    return render ( request, 'skillCrud.html', {
        "skills":skills,
        "skillsImages":skillsImages,
    })

@login_required
def crudSkillCreate(request):
    if request.method == "GET":
        return render(request, 'skillCrudCreate.html', {
            'skillForm': SkillsForm(),
            'skillImageForm': SkillsImageForm(),
        })
    else:
        try:
            formSkill = SkillsForm(request.POST, request.FILES)
            new_skill = formSkill.save(commit=False)
            new_skill.user = request.user
            new_skill.save()

            programingLanguageImages = request.FILES.getlist('programingLanguageImages')
            userInterfaceImages = request.FILES.getlist('userInterfaceImages')
            developmentToolsImages = request.FILES.getlist('developmentToolsImages')
            databasesImages = request.FILES.getlist('databasesImages')
            dataProcessingImages = request.FILES.getlist('dataProcessingImages')
            operatingSystemsImages = request.FILES.getlist('operatingSystemsImages')

            for image in programingLanguageImages:
                new_image = SkillsImages(programingLanguageImages=image)
                new_image.skills = new_skill
                new_image.save()

            for image in userInterfaceImages:
                new_image = SkillsImages(userInterfaceImages=image)
                new_image.skills = new_skill
                new_image.save()

            for image in developmentToolsImages:
                new_image = SkillsImages(developmentToolsImages=image)
                new_image.skills = new_skill
                new_image.save()
                
            for image in databasesImages:
                new_image = SkillsImages(databasesImages=image)
                new_image.skills = new_skill
                new_image.save()
            
            for image in dataProcessingImages:
                new_image = SkillsImages(dataProcessingImages=image)
                new_image.skills = new_skill
                new_image.save()
            
            for image in operatingSystemsImages:
                new_image = SkillsImages(operatingSystemsImages=image)
                new_image.skills = new_skill
                new_image.save()

            return redirect("crud")
        except:
            return render(request, 'skillCrudCreate.html', {
                'skillForm': SkillsForm(),
                'skillImageForm': SkillsImageForm(),
                'error': 'Por favor, proporciona datos válidos'
            })

@login_required
def crudSkillUpdate(request, pk):
    skill = Skill.objects.get(pk=pk)
    print(skill)
    if request.method == "GET":
        skillForm = SkillsForm(instance=skill)
        skillImageForm = SkillsImageForm(instance=skill)

    else:
        skillForm = SkillsForm(request.POST, request.FILES, instance=skill)
        if skillForm.is_valid():
            new_product = skillForm.save(commit=False)
            new_product.save()

            programingLanguageImages = request.FILES.getlist('programingLanguageImages')
            userInterfaceImages = request.FILES.getlist('userInterfaceImages')
            developmentToolsImages = request.FILES.getlist('developmentToolsImages')
            databasesImages = request.FILES.getlist('databasesImages')
            dataProcessingImages = request.FILES.getlist('dataProcessingImages')
            operatingSystemsImages = request.FILES.getlist('operatingSystemsImages')

            if programingLanguageImages:
                images = skill.images.filter(skills_id=skill, programingLanguageImages__isnull=False).values('programingLanguageImages')
                filtered_images = images.exclude(programingLanguageImages="")
                image_ids = filtered_images.values_list('id', flat=True)

                if image_ids:
                    for value1 in image_ids:

                        images_to_delete = SkillsImages.objects.filter(id=value1)
                        images_to_delete.delete()

                    if programingLanguageImages:
                        for image in programingLanguageImages:
                            new_image = SkillsImages(programingLanguageImages=image)
                            new_image.skills = skill
                            new_image.save()
                else:
                    if programingLanguageImages:
                        
                        for image in programingLanguageImages:
                            new_image = SkillsImages(programingLanguageImages=image)
                            new_image.skills = skill
                            new_image.save()
                        
            if userInterfaceImages:
                images = skill.images.filter(skills_id=skill, userInterfaceImages__isnull=False).values('userInterfaceImages')
                filtered_images = images.exclude(userInterfaceImages="")
                image_ids = filtered_images.values_list('id', flat=True)

                if image_ids:
                    for value1 in image_ids:

                        images_to_delete = SkillsImages.objects.filter(id=value1)
                        images_to_delete.delete()

                    if userInterfaceImages:
                        for image in userInterfaceImages:
                            new_image = SkillsImages(userInterfaceImages=image)
                            new_image.skills = skill
                            new_image.save()
                else:
                    if userInterfaceImages:
                        for image in userInterfaceImages:
                            new_image = SkillsImages(userInterfaceImages=image)
                            new_image.skills = skill
                            new_image.save()
            
            if developmentToolsImages:
                images = skill.images.filter(skills_id=skill, developmentToolsImages__isnull=False).values('developmentToolsImages')
                filtered_images = images.exclude(developmentToolsImages="")
                image_ids = filtered_images.values_list('id', flat=True)

                if image_ids:
                    for value1 in image_ids:

                        images_to_delete = SkillsImages.objects.filter(id=value1)
                        images_to_delete.delete()

                    if developmentToolsImages:
                        for image in developmentToolsImages:
                            new_image = SkillsImages(developmentToolsImages=image)
                            new_image.skills = skill
                            new_image.save()
                else:
                    if developmentToolsImages:
                        for image in developmentToolsImages:
                            new_image = SkillsImages(developmentToolsImages=image)
                            new_image.skills = skill
                            new_image.save()
                            
            if databasesImages:
                images = skill.images.filter(skills_id=skill, databasesImages__isnull=False).values('databasesImages')
                filtered_images = images.exclude(databasesImages="")
                image_ids = filtered_images.values_list('id', flat=True)

                if image_ids:
                    for value1 in image_ids:

                        images_to_delete = SkillsImages.objects.filter(id=value1)
                        images_to_delete.delete()

                    if databasesImages:
                        for image in databasesImages:
                            new_image = SkillsImages(databasesImages=image)
                            new_image.skills = skill
                            new_image.save()
                else:
                    if databasesImages:
                        for image in databasesImages:
                            new_image = SkillsImages(databasesImages=image)
                            new_image.skills = skill
                            new_image.save()
                            
            if dataProcessingImages:
                images = skill.images.filter(skills_id=skill, dataProcessingImages__isnull=False).values('dataProcessingImages')
                filtered_images = images.exclude(dataProcessingImages="")
                image_ids = filtered_images.values_list('id', flat=True)

                if image_ids:
                    for value1 in image_ids:

                        images_to_delete = SkillsImages.objects.filter(id=value1)
                        images_to_delete.delete()

                    if dataProcessingImages:
                        for image in dataProcessingImages:
                            new_image = SkillsImages(dataProcessingImages=image)
                            new_image.skills = skill
                            new_image.save()
                else:
                    if dataProcessingImages:
                        for image in dataProcessingImages:
                            new_image = SkillsImages(dataProcessingImages=image)
                            new_image.skills = skill
                            new_image.save()
                            
            if operatingSystemsImages:
                images = skill.images.filter(skills_id=skill, operatingSystemsImages__isnull=False).values('operatingSystemsImages')
                filtered_images = images.exclude(operatingSystemsImages="")
                image_ids = filtered_images.values_list('id', flat=True)

                if image_ids:
                    for value1 in image_ids:

                        images_to_delete = SkillsImages.objects.filter(id=value1)
                        images_to_delete.delete()

                    if operatingSystemsImages:
                        for image in operatingSystemsImages:
                            new_image = SkillsImages(operatingSystemsImages=image)
                            new_image.skills = skill
                            new_image.save()
                else:
                    if operatingSystemsImages:
                        for image in operatingSystemsImages:
                            new_image = SkillsImages(operatingSystemsImages=image)
                            new_image.skills = skill
                            new_image.save()
            
            
            return redirect("crudSkill")
    
    return render(request, 'skillCrudUpdate.html', {
            'skillForm': skillForm,
            'skillImageForm': skillImageForm,
    })

@login_required
def crudSkillDelete(request, pk):
    skill = Skill.objects.get(pk=pk)
    skill.delete()

    return redirect("crudSkill")

@login_required
def crudBlog(request):
    blogCategory = BlogCategory.objects.all()
    blogFile = BlogFile.objects.all()
    return render ( request, 'blogCrud.html', {
        "blogCategories":blogCategory,
        "blogFiles":blogFile,
    })

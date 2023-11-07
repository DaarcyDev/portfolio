from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Skill, About, Project, SkillsImages, ProjectImages, BlogCategory, BlogFile, Contact
from .forms import AboutForm, ProjectForm, ProjectImageForm, SkillsForm, SkillsImageForm, BlogCategoryForm, BlogFileForm, ContactForm
from django.shortcuts import get_object_or_404
from django.forms import modelformset_factory
from django.views.decorators.csrf import csrf_protect
import resend

# @csrf_protect
def index(request):
    about = About.objects.all()
    skills = Skill.objects.all()
    skillsImage = SkillsImages.objects.all()
    projects = Project.objects.all()
    projectImages = ProjectImages.objects.all()
    blogCategory = BlogCategory.objects.all()
    blogFile = BlogFile.objects.all()
    contact = Contact.objects.all()
    mensaje = ""
    
    
    if request.method == 'POST':
        print(request.method)
        # nombre = request.POST.get('nombre')
        # telefono = request.POST.get('telefono')
        # correo = request.POST.get('correo')
        # mensaje = request.POST.get('mensaje')

        # correo_receptor = 'liam_alvarez@hotmail.com'
        # correo_emisor = 'delivered@resend.dev'
        # asunto = 'Nuevo mensaje desde tu sitio web; Nombre: ' + nombre + ", Telefono: " + telefono
        # mensaje_correo = f'Nombre: {nombre}\nTeléfono: {telefono}\nCorreo: {correo}\nMensaje: {mensaje}'

        # resend.api_key = "re_V3tUaG1T_6ms36RbTJh81pfEML3gSkRJ8"

        # r = resend.Emails.send({
        #     "from": correo_emisor,
        #     "to": correo_receptor,
        #     "subject": asunto,
        #     "html": mensaje_correo
        # })
        # if r:
        mensaje = '¡El correo se envió con éxito!'
        # else:
        #     mensaje = ""

    return render(request, 'index.html', {
            "abouts": about,
            "projects": projects,
            "skills": skills,
            "skillsImages": skillsImage,
            "projectImages": projectImages,
            "blogCategories": blogCategory,
            "blogFiles": blogFile,
            "contacts": contact,
            "message": mensaje
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
    # print(skill)
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

@login_required
def crudBlogCreate(request):
    if request.method == "GET":
        blogCategoryForm = BlogCategoryForm()
        BlogFileFormSet = modelformset_factory(BlogFile, form=BlogFileForm, extra=1)
        blogFileFormSet = BlogFileFormSet(queryset=BlogFile.objects.none())
    else:
        try:
            blogCategoryForm = BlogCategoryForm(request.POST)
            if blogCategoryForm.is_valid():
                new_category = blogCategoryForm.save(commit=False)
                new_category.user = request.user
                new_category.save()

                BlogFileFormSet = modelformset_factory(BlogFile, form=BlogFileForm, extra=1)
                blogFileFormSet = BlogFileFormSet(request.POST, request.FILES, queryset=BlogFile.objects.none())

                if blogFileFormSet.is_valid():
                    for blogFileForm in blogFileFormSet:
                        if blogFileForm.cleaned_data:
                            new_file = blogFileForm.save(commit=False)
                            new_file.category = new_category
                            new_file.user = request.user
                            new_file.save()

                    return redirect("crudBlog")

        except:
            return render(request, 'blogCrudCreate.html', {
                'blogCategoryForm': BlogCategoryForm,
                'blogFileFormSet': blogFileFormSet,
                'error': 'Please provide valid data'
            })

    return render(request, 'blogCrudCreate.html', {
        'blogCategoryForm': blogCategoryForm,
        'blogFileFormSet': blogFileFormSet,
    })
    
@login_required
def crudBlogUpdate(request, pk):
    try:
        blog_category = BlogCategory.objects.get(pk=pk)

        if request.method == "GET":
            blog_category_form = BlogCategoryForm(instance=blog_category)
            BlogFileFormSet = modelformset_factory(BlogFile, form=BlogFileForm, extra=1)
            blog_file_formset = BlogFileFormSet(queryset=blog_category.blog_files.all())

        else:
            blog_category_form = BlogCategoryForm(request.POST, instance=blog_category)

            if blog_category_form.is_valid():
                updated_category = blog_category_form.save()

                BlogFileFormSet = modelformset_factory(BlogFile, form=BlogFileForm, extra=1)
                blog_file_formset = BlogFileFormSet(request.POST, request.FILES, queryset=updated_category.blog_files.all())

                if blog_file_formset.is_valid():
                    for blog_file_form in blog_file_formset:
                        if blog_file_form.cleaned_data:
                            updated_file = blog_file_form.save(commit=False)
                            updated_file.category = updated_category
                            updated_file.save()

                    return redirect("crudBlog")

    except BlogCategory.DoesNotExist:
        return render(request, 'crud.html')

    return render(request, 'blogCrudUpdate.html', {
        'blogCategoryForm': blog_category_form,
        'blogFileFormSet': blog_file_formset,
        'blogCategory': blog_category,
    })

@login_required
def crudBlogDelete(request, pk):
    blog = BlogCategory.objects.get(pk=pk)
    blog.delete()

    return redirect("crudBlog")

@login_required
def crudContact(request):
    contact = Contact.objects.all()
    return render ( request, 'contactCrud.html', {
        "contacts":contact,
    })

@login_required
def crudContactCreate(request):
    if(request.method == "GET"):
        return render(request, 'contactCrudCreate.html', {
            'formContacts': ContactForm,
        })
    else:
        try:
            formContact = ContactForm(request.POST, request.FILES)
            new_product = formContact.save(commit=False)
            new_product.save()
            return redirect("crudContact")
        except:
            return render(request, 'contactCrudCreate.html',{
            'formContacts': ContactForm,
            'error': 'please provide valide data'
        })

@login_required
def crudContactDelete(request, pk):
    contact = Contact.objects.get(pk=pk)
    contact.delete()

    return redirect("crudContact")

@login_required
def crudContactUpdate(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == "GET":
        formContact = ContactForm(instance=contact)

    else:
        try:
            formContact = ContactForm(request.POST, request.FILES, instance=contact)
            new_product = formContact.save(commit=False)
            new_product.save()
            return redirect("crudContact")
        except:
            return render(request, 'contactCrudUpdate.html',{
                'formContacts': formContact,
                'error': 'please provide valide data'
            })
    return render(request, 'contactCrudUpdate.html', {
        'formContacts': formContact,
    })

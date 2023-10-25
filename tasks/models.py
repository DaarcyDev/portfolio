from django.db import models

# Modelo para la sección "About"
class About(models.Model):
    aboutResume = models.CharField(max_length=500)
    aboutComplete = models.TextField()
    aboutImages = models.ImageField(upload_to='about_images/', blank=True, null=True)
    
# Modelo para la sección "Projects"
class Project(models.Model):
    projectResume = models.CharField(max_length=500, blank=True)
    projectComplete = models.TextField(blank=True)
    projectImage = models.ImageField(upload_to='project_images/')
    projectWebsiteResume = models.TextField()
    # projectWebsiteImages = models.ImageField(upload_to='project_website_images/')
    projectWebsiteUrl = models.URLField()
    # projectWebsiteTools = models.ImageField(upload_to='project_website_images_tools/')

class ProjectImages(models.Model):
    projectWebsiteImages = models.ImageField(upload_to='project_website_images/',blank=True)
    projectWebsiteTools = models.ImageField(upload_to='project_website_images_tools/',blank=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    

# Modelo para la sección "Skills"
class Skill(models.Model):
    skillsResume = models.CharField(max_length=500,blank=True)
    skillComplete = models.TextField(blank=True)
    programingLanguageResume = models.TextField()
    # programingLanguageImages = models.ImageField(upload_to='programming_language_images/')
    userInterfaceResume = models.TextField()
    # userInterfaceImages = models.ImageField(upload_to='user_interface_images/')
    developmentToolsResume = models.TextField()
    # developmentToolsImages = models.ImageField(upload_to='development_tools_images/')
    databasesResume = models.TextField()
    # databasesImages = models.ImageField(upload_to='databases_images/')
    dataProcessingResume = models.TextField()
    # dataProcessingImages = models.ImageField(upload_to='data_processing_images/')
    operatingSystemsResume = models.TextField()
    # operatingSystemsImages = models.ImageField(upload_to='operating_systems_images/')

class SkillsImages(models.Model):
    programingLanguageImages = models.ImageField(upload_to='programming_language_images/', blank=True)
    userInterfaceImages = models.ImageField(upload_to='user_interface_images/', blank=True)
    developmentToolsImages = models.ImageField(upload_to='development_tools_images/', blank=True)
    databasesImages = models.ImageField(upload_to='databases_images/', blank=True)
    dataProcessingImages = models.ImageField(upload_to='data_processing_images/', blank=True)
    operatingSystemsImages = models.ImageField(upload_to='operating_systems_images/', blank=True)
    skills = models.ForeignKey(Skill,on_delete=models.CASCADE)

# Modelo para la sección "Blog"
class BlogCategory(models.Model):
    name = models.CharField(max_length=500)
    blogResume = models.CharField(max_length=500, blank=True)

class BlogFile(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blog_files')
    file = models.CharField(max_length=255)  # Cambiamos a CharField
    fileContent = models.TextField()

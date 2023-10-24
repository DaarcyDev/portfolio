from django.db import models

# Modelo para la sección "About"
class About(models.Model):
    aboutResume = models.CharField(max_length=500)
    aboutComplete = models.TextField()
    aboutImages = models.ImageField(upload_to='about_images/', blank=True, null=True)
    
# Modelo para la sección "Projects"
class Project(models.Model):
    projectResume = models.CharField(max_length=500)
    projectComplete = models.TextField()
    projectImages = models.ImageField(upload_to='project_images/')
    projectWebsiteResume = models.TextField()
    projectWebsiteImages = models.ImageField(upload_to='project_website_images/')
    projectWebsiteUrl = models.URLField()
    projectWebsiteTools = models.TextField()

# Modelo para la sección "Skills"
class Skill(models.Model):
    skillsResume = models.CharField(max_length=500)
    skillComplete = models.TextField()
    programingLanguageResume = models.TextField()
    programingLanguageImages = models.ImageField(upload_to='programming_language_images/')
    userInterfaceResume = models.TextField()
    userInterfaceImages = models.ImageField(upload_to='user_interface_images/')
    developmentToolsResume = models.TextField()
    developmentToolsImages = models.ImageField(upload_to='development_tools_images/')
    databasesResume = models.TextField()
    databasesImages = models.ImageField(upload_to='databases_images/')
    dataProcessingResume = models.TextField()
    dataProcessingImages = models.ImageField(upload_to='data_processing_images/')
    operatingSystemsResume = models.TextField()
    operatingSystemsImages = models.ImageField(upload_to='operating_systems_images/')

# Modelo para la sección "Blog"
class Blog(models.Model):
    blogCategories = models.CharField(max_length=500)
    blogFile = models.FileField(upload_to='blog_files/')
    blogFileContent = models.TextField()


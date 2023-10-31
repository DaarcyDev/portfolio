from django.db import models

class About(models.Model):
    aboutResume = models.CharField(max_length=500)
    aboutComplete = models.TextField()
    aboutImages = models.ImageField(upload_to='about_images/', blank=True, null=True)

    def __str__(self):
        return self.aboutResume
    
    
class Project(models.Model):
    projectResume = models.CharField(max_length=500, blank=True)
    projectComplete = models.TextField(blank=True)
    projectName = models.CharField(max_length=500, blank=True)
    projectImage = models.ImageField(upload_to='project_images/')
    projectWebsiteResume = models.TextField()
    projectWebsiteUrl = models.URLField()
    
    def __str__(self):
        return self.projectName
    

class ProjectImages(models.Model):
    projectWebsiteImages = models.FileField(upload_to='project_website_images/',blank=True)
    projectWebsiteTools = models.FileField(upload_to='project_website_images_tools/',blank=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name="images")
    
    def __str__(self):
        return self.project.projectName

class Skill(models.Model):
    skillsResume = models.CharField(max_length=500,blank=True)
    skillComplete = models.TextField(blank=True)
    programingLanguageResume = models.TextField()
    userInterfaceResume = models.TextField()
    developmentToolsResume = models.TextField()
    databasesResume = models.TextField()
    dataProcessingResume = models.TextField()
    operatingSystemsResume = models.TextField()
    
    def __str__(self):
        return self.skillsResume

class SkillsImages(models.Model):
    programingLanguageImages = models.ImageField(upload_to='programming_language_images/', blank=True)
    userInterfaceImages = models.ImageField(upload_to='user_interface_images/', blank=True)
    developmentToolsImages = models.ImageField(upload_to='development_tools_images/', blank=True)
    databasesImages = models.ImageField(upload_to='databases_images/', blank=True)
    dataProcessingImages = models.ImageField(upload_to='data_processing_images/', blank=True)
    operatingSystemsImages = models.ImageField(upload_to='operating_systems_images/', blank=True)
    skills = models.ForeignKey(Skill,on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return self.skills.skillsResume
    
    
class BlogCategory(models.Model):
    name = models.CharField(max_length=500)
    blogResume = models.CharField(max_length=500, blank=True)
    
    def __str__(self):
        return self.name

class BlogFile(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blog_files')
    file = models.CharField(max_length=255) 
    fileContent = models.TextField()
    
    def __str__(self):
        return self.file

class Contact(models.Model):
    contactResume = models.CharField(max_length=500)
    contactComplete = models.TextField()
    youtubeUrl = models.URLField()
    instagramUrl = models.URLField()
    githubUrl = models.URLField()
    linkedinUrl = models.URLField()
    youtubeImage = models.ImageField(upload_to='contact_images/', blank=True)
    instagramImage = models.ImageField(upload_to='contact_images/', blank=True)
    githubImage = models.ImageField(upload_to='contact_images/', blank=True)
    linkedinImage = models.ImageField(upload_to='contact_images/', blank=True)
    
    def __str__(self):
        return self.contactResume

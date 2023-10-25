from django.contrib import admin
from .models import Skill, About, Project, BlogCategory, BlogFile, ProjectImages, SkillsImages

# Define an inline class for ProjectImages
class ProjectImagesInline(admin.TabularInline):
    model = ProjectImages

# Define the ProjectAdmin class
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImagesInline]  # Add the ProjectImagesInline inline to the ProjectAdmin

class SkillsImagesInline(admin.TabularInline):
    model = SkillsImages

# Define the SkillsAdmin class
class SkillsAdmin(admin.ModelAdmin):
    inlines = [SkillsImagesInline]  # Add the ProjectImagesInline inline to the ProjectAdmin

class BlogFileInline(admin.TabularInline):
    model = BlogFile

class BlogFileAdmin(admin.ModelAdmin):
    inlines = [BlogFileInline]  # Add the ProjectImagesInline inline to the ProjectAdmin

# Register your models
admin.site.register(Skill, SkillsAdmin)
admin.site.register(About)
admin.site.register(BlogCategory, BlogFileAdmin)
admin.site.register(Project, ProjectAdmin)  # Register the ProjectAdmin with Project model

from django.contrib import admin
from .models import Skill, About, Project, BlogCategory, BlogFile, ProjectImages, SkillsImages, Contact

class ProjectImagesInline(admin.TabularInline):
    model = ProjectImages

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImagesInline]  

class SkillsImagesInline(admin.TabularInline):
    model = SkillsImages

class SkillsAdmin(admin.ModelAdmin):
    inlines = [SkillsImagesInline]  

class BlogFileInline(admin.TabularInline):
    model = BlogFile

class BlogFileAdmin(admin.ModelAdmin):
    inlines = [BlogFileInline]  

admin.site.register(Skill, SkillsAdmin)
admin.site.register(About)
admin.site.register(BlogCategory, BlogFileAdmin)
admin.site.register(Project, ProjectAdmin) 
admin.site.register(Contact)

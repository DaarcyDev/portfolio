from django import forms
from .models import About,Project, ProjectImages, Skill, SkillsImages
from django.forms import ClearableFileInput, FileField

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['aboutResume', 'aboutComplete', 'aboutImages']


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True



class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['projectResume', 'projectComplete', 'projectName', 'projectImage', 'projectWebsiteResume', 'projectWebsiteUrl']


class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = ProjectImages
        fields = ['projectWebsiteImages', 'projectWebsiteTools']
        widgets = {
            'projectWebsiteImages': MultipleFileInput(attrs={'multiple': True}),
            'projectWebsiteTools': MultipleFileInput(attrs={'multiple': True}),
        }

class SkillsForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = ['skillsResume', 'skillComplete', 'programingLanguageResume', 'userInterfaceResume', 'developmentToolsResume', 'databasesResume',"dataProcessingResume","operatingSystemsResume"]


class SkillsImageForm(forms.ModelForm):
    class Meta:
        model = SkillsImages
        fields = ['programingLanguageImages', 'userInterfaceImages','developmentToolsImages',"databasesImages","dataProcessingImages","operatingSystemsImages"]
        widgets = {
            'programingLanguageImages': MultipleFileInput(attrs={'multiple': True}),
            'userInterfaceImages': MultipleFileInput(attrs={'multiple': True}),
            'developmentToolsImages': MultipleFileInput(attrs={'multiple': True}),
            'databasesImages': MultipleFileInput(attrs={'multiple': True}),
            'dataProcessingImages': MultipleFileInput(attrs={'multiple': True}),
            'operatingSystemsImages': MultipleFileInput(attrs={'multiple': True}),
        }


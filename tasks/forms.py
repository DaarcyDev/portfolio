from django import forms
from .models import About,Project, ProjectImages
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


from django import forms
from .models import About,Project, ProjectImages
from django.forms import ClearableFileInput, FileField

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['aboutResume', 'aboutComplete', 'aboutImages']

# class ProjectAndImagesForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = ['projectResume', 'projectComplete', 'projectName', 'projectImage', 'projectWebsiteResume', 'projectWebsiteUrl', 'image']
#         widgets = {
#             'image': ClearableFileInput(attrs={'multiple': True}),
#         }

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

# class MultipleFileInput(forms.ClearableFileInput):
#     template_name = 'your_template_name.html'

#     def get_context(self, name, value, attrs):
#         context = super().get_context(name, value, attrs)
#         context['widget']['attrs'].update({'multiple': True})
#         return context

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


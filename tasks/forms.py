from django.forms import ModelForm 
from django import forms
# from .models import 

class CreateAbout(forms.Form):
    aboutResume = models.CharField(label="about_resume", max_length=500)
    aboutComplete = models.TextField(widget=forms.Textarea)
    aboutImages = models.ImageField(upload_to='about_images/', blank=True, null=True)
    

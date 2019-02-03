from django import forms
from .models import UserProject

class UserProjectForm(forms.ModelForm):
    class Meta:
        model = UserProject
        exclude = ('user',)
        fields = ['name','funds_Required','domain','Project_Description','image1','image2','image3','image4','contributors','ongoing']

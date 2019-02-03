from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomInvestor, CustomDeveloper,CustomUser
from django import forms

class CustomInvestorCreationForm(forms.ModelForm):
    class Meta:
        model = CustomInvestor
        fields = ('company_name', 'city', 'designation', 'linkedin_id', 'contact_no')
   
        

class CustomInvestorChangeForm(UserChangeForm):
    class Meta:
        model = CustomInvestor
        fields = ('user','company_name', 'city', 'designation', 'linkedin_id', 'contact_no')

class CustomDeveloperCreationForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = CustomDeveloper
        fields = ('institute_name', 'city', 'linkedin_id', 'contact_no')
     



class CustomDeveloperChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomDeveloper
        fields = ('user', 'institute_name', 'city', 'linkedin_id', 'contact_no')

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email','user_type')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'email','user_type')
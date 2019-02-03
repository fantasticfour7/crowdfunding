from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomInvestorChangeForm, CustomInvestorCreationForm, CustomDeveloperCreationForm, CustomDeveloperChangeForm,CustomUserCreationForm, CustomUserChangeForm
from .models import CustomInvestor, CustomUser, CustomDeveloper

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username','email','user_type']

class CustomInvestorAdmin(admin.ModelAdmin):
    add_form = CustomInvestorCreationForm
    form = CustomInvestorChangeForm
    list_display = ['company_name','city']
    model = CustomInvestor

class CustomDeveloperAdmin(admin.ModelAdmin):
    add_form = CustomDeveloperCreationForm
    form = CustomDeveloperChangeForm
    list_display = ['institute_name','city']
    model = CustomDeveloper


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomInvestor,CustomInvestorAdmin)
admin.site.register(CustomDeveloper,CustomDeveloperAdmin)

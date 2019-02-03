from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    choices = [
        ('A','Investor'),
        ('B','Developer'),
    ]
    user_type = models.CharField(choices = choices, default = 'None', blank = False, max_length = 50)
    
class CustomInvestor(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, blank = True)
    company_name = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    designation = models.CharField(max_length = 50)
    linkedin_id = models.CharField(max_length = 50)
    contact_no = models.CharField(max_length = 10)
    donated_to = models.CharField(max_length=500, default = '')

class CustomDeveloper(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, blank = True)
    institute_name = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    linkedin_id = models.CharField(max_length = 50)
    contact_no = models.CharField(max_length = 10)

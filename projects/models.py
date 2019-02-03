from django.db import models

#domain choices
Domain_Choices = [
    ('1', ('Agriculture')),
    ('2', ('Business')),
    ('3', ('Computer')),
    ('4', ('Civil')),
    ('5', ('Performing Arts')),
    ('6', ('Electrical')),
    ('7', ('Biotechnology')),
    ('8', ('Biomedical')),
    ('9', ('Electronics')),
    ('10', ('Mechanical')),
    ('11', ('Chemical')),
    ('12', ('Cinematography')),
    ('13', ('Educational')),
]

# class for Student projects
class UserProject(models.Model):
    owner = models.ForeignKey('accounts.CustomUser',related_name='project', on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    funds_Required = models.PositiveIntegerField()
    domain = models.CharField(choices = Domain_Choices, default = False, blank = False, max_length = 10 )
    Project_Description  = models.TextField()
    image1 = models.FileField()
    image2 = models.FileField()
    image3 = models.FileField()
    image4 = models.FileField()
    contributors = models.CharField(max_length = 300)
    ongoing = models.BooleanField(default = False)

    def __str__(self):
        return self.name
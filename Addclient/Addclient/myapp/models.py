
from django.db import models

class Add_requirement(models.Model):
    COMPANY_NAME = models.CharField(max_length=255,default='COMPANY_NAME')
    URL = models.URLField(default='URL')
    Address_1 = models.CharField(max_length=255,default='Address_1')
    Address_2 = models.CharField(max_length=255,default='Address_2')
    Country = models.CharField(max_length=255,default='Country')
    State = models.CharField(max_length=255,default='State')
    City = models.CharField(max_length=255,default='City')
    Zip = models.CharField(max_length=255,default='Zip')
    Industry = models.CharField(max_length=255,default='Industry')
    Company_Size = models.CharField(max_length=255,default='Company_Size')
    Linkedin = models.CharField(max_length=255,default='Linkedin')
    Networth = models.CharField(max_length=255,default='Networth')

    # def __str__(self):
    #     return self.title_for_req
 
 

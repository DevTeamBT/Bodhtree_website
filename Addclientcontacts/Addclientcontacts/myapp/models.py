from django.db import models

class Add_requirement(models.Model):
    Select_Company = models.CharField(max_length=255,default='Select_Company')
    Select_Country = models.CharField(max_length=255,default='Select_Country')
    Select_State = models.CharField(max_length=255,default='Select_State')
    Select_City = models.CharField(max_length=255,default='Select_City')
    First_Name = models.CharField(max_length=255,default='First_Name')
    Last_Name = models.CharField(max_length=255,default='Last_Name')
    Job_Title = models.CharField(max_length=255,default='Job_Title')
    Department = models.CharField(max_length=255,default='Department')
    Email_Id = models.CharField(max_length=255,default='Email_Id')
    Mobile_No = models.CharField(max_length=255,default='Mobile_No')
    Linkedin = models.CharField(max_length=255,default='Linkedin')
    Select_Source = models.CharField(max_length=255,default='Select_Source')
 
 

 
 

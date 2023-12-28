
from django.db import models

class Add_requirement(models.Model):
    requirement = models.CharField(max_length=255,default='requirement')
    client = models.CharField(max_length=255,default='client')
    contact= models.CharField(max_length=255,default='contact')
    accountmgr= models.CharField(max_length=255,default='accountmgr')
    candidatename = models.CharField(max_length=255,default='candidatename')
    currentcompany = models.CharField(max_length=255,default='currentcompany')
    mobileno = models.CharField(max_length=255,default='mobileno')
    emailid = models.CharField(max_length=255,default='emailid')
    currentctc= models.CharField(max_length=255,default='currentctc')
    expectedctc= models.CharField(max_length=255,default='expectedctc')
    noticeperiod= models.CharField(max_length=255,default='noticeperiod')
    locationpreference = models.CharField(max_length=255,default='locationpreference')
    location = models.CharField(max_length=255,default='location')
    hiretype = models.CharField(max_length=255,default='hiretype')
    worktype= models.CharField(max_length=255,default='worktype')
    recruiter = models.CharField(max_length=255,default='recruiter')
    selAccmanager = models.CharField(max_length=255,default='selAccmanager')
    position = models.CharField(max_length=255,default='position')

    # def __str__(self):
    #     return self.title_for_req
 
 

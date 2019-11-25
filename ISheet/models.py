from django.db import models
from django.contrib.auth.models import User

class contact():
    id = models.CharField(max_length=5)
    ImgName = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    passion = models.CharField(max_length=100)
    mailid = models.CharField(max_length=100)

class form_IS(models.Model):
    pd_country = models.CharField(max_length=100,null=True)
    pd_Plat_methodology = models.CharField(max_length=100,null=True)

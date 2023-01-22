from django.db import models

# Create your models here.

# Create your models here.
class customerdetails(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    Email= models.CharField(max_length=100,null=True,blank=True)
    Password = models.CharField(max_length=30, null=True, blank=True)
    Confirm_Password = models.CharField(max_length=30, null=True, blank=True)

class pagedb(models.Model):
    First_Name = models.CharField(max_length=100, null=True, blank=True)
    Last_Name = models.CharField(max_length=100, null=True, blank=True)
    Date = models.IntegerField(null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)


from django.db import models

# Create your models here.

class studentbb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100,null=True,blank=True)
    Password = models.CharField(max_length=50,null=True,blank=True)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,null=True,blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
    City = models.CharField(max_length=100,null=True,blank=True)
    Address = models.CharField(max_length=100,null=True,blank=True)

class regdb(models.Model):
    Category_Name = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)

class prodb(models.Model):
    Category_Name = models.CharField(max_length=30, null=True, blank=True)
    Product_Name = models.CharField(max_length=30, null=True, blank=True)
    Product_Price = models.IntegerField(null=True, blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Description = models.CharField(max_length=30, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)



class cndb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)
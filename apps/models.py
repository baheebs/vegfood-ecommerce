from django.db import models

# Create your models here.
class customer(models.Model):
    objects = None
    Name = models.CharField(max_length=100, null=True, blank=True)
    Contactnumber = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)

class category(models.Model):
    objects = None
    Name = models.CharField(max_length=100, null=True, blank=True)
    Desc = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)


class proddetails(models.Model):
    objects = None
    Name = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField()
    category = models.CharField(max_length=100, null=True, blank=True)
    Desc = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)

class msgdb(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    mail = models.EmailField(max_length=100, null=True, blank=True)
    sub =  models.CharField(max_length=100, null=True, blank=True)
    messge = models.CharField(max_length=100, null=True, blank=True)
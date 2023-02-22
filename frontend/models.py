from django.db import models

# Create your models here.
class registerdb(models.Model):

    name = models.CharField(max_length=100, null=True, blank=True)
    mail = models.EmailField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    conpassword = models.CharField(max_length=100, null=True, blank=True)

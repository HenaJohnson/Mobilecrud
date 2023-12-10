from django.db import models

# Create your models here.

class Mobilemodel(models.Model):

    brand = models.CharField(max_length=20)
    modls= models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    price = models.PositiveIntegerField(null=True)
    year = models.PositiveIntegerField(null=True)



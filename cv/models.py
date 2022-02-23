from django.db import models


# Create your models here.

class Profil(models.Model):
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    year = models.DateField(auto_now=False, auto_now_add=False)
    license = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)

from django.db import models


class Profil(models.Model):
    image = models.ImageField(),
    first_name = models.CharField(max_length=30),
    last_name = models.CharField(max_length=30),
    description = models.TextField(max_length=2000),


class Competencie(models.Model):
    PERCENTAGE = (
        ('60', 'Little'),
        ('80', 'Medium'),
        ('100', 'Lot'),
    ),
    name = models.CharField(max_length=100),
    percentage = models.CharField(max_length=1, choices=PERCENTAGE),


class Experience(models.Model):
    post = models.CharField(max_length=100),
    company = models.CharField(max_length=100),
    date_start = models.DateField(),
    date_end = models.DateField(),
    description = models.TextField(max_length=2000),


class Formation(models.Model):
    name = models.CharField(max_length=100),
    location = models.CharField(max_length=100),
    date_start = models.DateField(),
    date_end = models.DateField(),
    description = models.TextField(max_length=2000),


class Contact(models.Model):
    icon = models.CharField(max_length=100),
    title = models.CharField(max_length=100),




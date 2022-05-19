from turtle import update
from django.db import models

# Create your models here.

class Site(models.Model):
    name_site =models.CharField(max_length=50)
    session_img_banner_site = models.URLField()
    adresse_site =models.CharField(max_length=50)
    phone_site = models.IntegerField()
    email_site = models.EmailField(max_length=50)
    description_site = models.TextField(max_length=255)
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delele_at = models.DateTimeField(null=True)

class Banner(models.Model):
    libele_banner = models.CharField(max_length=50)
    description_banner = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delele_at = models.DateTimeField(null=True)

class Open_day(models.Model):
    jours_ouverture = models.DateField
    Hour_open = models.TimeField()
    hour_close = models.TimeField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delele_at = models.DateTimeField(null=True)

class Resau_social(models.Model):
    icon = models.CharField(max_length=50)
    name_reseau_social = models.CharField(max_length=30)
    links_reseau_social = models.CharField(max_length=255)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delele_at = models.DateTimeField(null=True)
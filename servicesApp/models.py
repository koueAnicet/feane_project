from django.db import models
from django.forms import FileField

# Create your models here.

class Categorie(models.Model):
    name_categorie = models.CharField(max_length=50)
    image_categorie = models.FileField(upload_to="Cate_imgs",)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delele_at = models.DateTimeField(null=True)

class Plat(models.Model):
    name_plat = models.CharField(max_length=50)
    prix_reduction_plat = models.IntegerField()
    description_plat =models.TextField()
    image_plat = models.FileField(upload_to= "plat_imgs")
    prix_plat = models.IntegerField()
    status_reduction_plat = models.BooleanField(default=False)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delele_at = models.DateTimeField(null=True)

class About(models.Model):
    image_about = models.FileField(upload_to= "plat_imgs")
    libele_about = models.CharField(max_length=50)
    descriptioni_about  = models.TextField(max_length=100)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delele_at = models.DateTimeField(null=True)
    def __str__(self):
        return self.libele_about
        
class Reservations(models.Model):
    name_reservation = models.CharField(max_length=30)
    num_reservation = models.IntegerField()
    email_reservation =models.EmailField(max_length=254)
    number_perso_reservation = models.IntegerField()
    date_reservation = models.DateTimeField
    maps_reservation =models.CharField(max_length=50)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delele_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name_reservation
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import * #PlatFavorie,About,About,

# Register your models here.

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):

    list_display = ('image', 'name_categorie', 'create_at', 'update_at', 'delele_at',)
    search_fields = ['name_categorie']
    def image(self, obj): 
        return mark_safe(f'<img src="{obj.image_categorie.url}" style="height:100px; width:200px">')
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):

    list_display = ('image', 'libele_about','descriptioni_about','create_at', 'update_at', 'delele_at',)
    search_fields = ['libele_about']
    def image(self, obj): 
        return mark_safe(f'<img src="{obj.image_about.url}" style="height:100px; width:200px">')

@admin.register(Plat)
class PlatAdmin(admin.ModelAdmin):

    list_display = ('image','name_plat','prix_reduction_plat','description_plat', 'prix_plat','create_at', 'update_at', 'delele_at','status_reduction_plat',)
    search_fields = ['name_plat']
    def image(self, obj): 
        return mark_safe(f'<img src="{obj.image_plat.url}" style="height:100px; width:200px">')
    

@admin.register(Reservations)
class ReservationsAdmin(admin.ModelAdmin):

    list_display = ('name_reservation','num_reservation','email_reservation', 'number_perso_reservation','date_reservation','maps_reservation','create_at', 'update_at', 'delele_at',)
    search_fields = ['name_reservation']
    

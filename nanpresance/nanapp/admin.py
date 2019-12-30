from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models
# Register your models here.
@admin.register(models.Profile)

class ProfilAdmin(admin.ModelAdmin):
    list_display=('my_image','user','contacts','genre','pays','ville','birth_date','date_add','date_update')
    list_filter=('user','genre','status')
    search_fields=('user',)
    list_display_links=('my_image','user')
    list_per_page=50
    ordering=['user']
    date_hierarchy=('date_add')
    readonly_fields=['detail_image']
    actions=('active','desactive')
    
    def active(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,'status active ;-)')
    active.short_description='active le status'
            
    def desactive(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,'status desactive  ;-(')
    active.short_description='active le status'
    
    def my_image(self,obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.images.url))
    
    def detail_image(self,obj):
        return mark_safe('<img src="{url}" width="400px" height="100px" />'.format(url=obj.images.url))
    
@admin.register(models.Qrcode)

class QrcodeAdmin(admin.ModelAdmin):
    list_display=('jours','created_by','debut_heure_arrivee','fin_heure_arrivee','titre_slug','status','created_at','updated_at')
    list_filter=('jours','created_by',)
    search_fields=('jours',)
    list_display_links=('jours','created_by')
    list_per_page=50
    date_hierarchy=('jours')
    ordering=['jours']


    
@admin.register(models.Presence)

class PresenceAdmin(admin.ModelAdmin):
    list_display=('etudiant','qrcode','heure_arrivee','heure_depart','status','created_at','updated_at')
    list_filter=('etudiant','heure_arrivee','heure_depart')
    search_fields=('etudiant',)
    list_display_links=('etudiant',)
    list_per_page=50
    ordering=['etudiant']
    date_hierarchy=('created_at')
from django.contrib import admin
from blog.models import Publicacion

# Register your models here.
class PublicacionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}
    list_display = ('titulo', 'publicado')
    ordering = ['-publicado']
    
admin.site.register(Publicacion, PublicacionAdmin)

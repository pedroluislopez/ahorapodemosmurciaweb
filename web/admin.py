from django.contrib import admin
from web.models import Candidato

# Register your models here.
class CandidatoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nombre', 'apellidos', 'orden', 'imagen']}),
        ('Candidatura', {'fields': ['secretario', 'consejo', 'motivacion']}),
    ]
    list_display = ('nombre', 'apellidos', 'secretario', 'consejo')
    ordering = ['orden']

admin.site.register(Candidato, CandidatoAdmin)
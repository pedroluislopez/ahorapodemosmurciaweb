from django.contrib import admin

from web.models import Candidato, IdeaFuerza, Cita, Documento


# Register your models here.
class CandidatoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nombre', 'apellidos', 'orden', 'imagen']}),
        ('Candidatura', {'fields': ['secretario', 'consejo', 'descripcion_corta', 'motivacion']}),
    ]
    list_display = ('nombre', 'apellidos', 'secretario', 'consejo')
    ordering = ['orden']
    
class IdeaFuerzaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'seccion', 'icono')
    ordering = ['orden']
    
class CitaAdmin(admin.ModelAdmin):
    list_display = ('get_candidato', 'orden')
    ordering = ['orden']
    
    def get_candidato(self, obj):
        return str(obj.candidato)
    
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')
    ordering = ['orden']

admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(IdeaFuerza, IdeaFuerzaAdmin)
admin.site.register(Cita, CitaAdmin)
admin.site.register(Documento, DocumentoAdmin)

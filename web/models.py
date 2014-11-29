# -*- encoding: utf-8 -*-

from django.db import models

# Create your models here.
class Candidato(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    apellidos  = models.CharField('Apellidos', max_length=50)
    imagen = models.ImageField('Imagen', upload_to='profile_images', blank=True)
    secretario = models.BooleanField('Secretario General', default=False)
    consejo = models.BooleanField('Consejo Ciudadano', default=False)
    motivacion = models.TextField('Motivación', max_length=1000, blank=True)
    orden = models.IntegerField('Orden')
    
    def __unicode__(self):
        return self.nombre + ' ' + self.apellidos
    
    def get_imagen(self):
        if not self.imagen:
            return 'http://placehold.it/200x200'
        return self.imagen.url
    
    def get_candidatura(self):
        if self.secretario:
            return 'Secretaría general'
        elif self.consejo:
            return 'Consejo ciudadano'
        else:
            return ''
    
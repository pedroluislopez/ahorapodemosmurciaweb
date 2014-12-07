# -*- encoding: utf-8 -*-

from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class Publicacion(models.Model):
    titulo = models.CharField('Título', max_length=255)
    slug = models.SlugField('Texto enlace', max_length=60, unique=True)
    entradilla = models.TextField('Entradilla', max_length=512)
    cuerpo = RichTextField('Cuerpo')
    publicado = models.DateField('Publicado')
    
    def __unicode__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
    
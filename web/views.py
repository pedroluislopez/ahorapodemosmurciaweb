from django.shortcuts import render
from web.models import Candidato, IdeaFuerza, Cita, Documento

# Create your views here.
def index(request):
    ideasfuerza_m = IdeaFuerza.objects.filter(seccion='m').order_by('orden')
    ideasfuerza_p = IdeaFuerza.objects.filter(seccion='p').order_by('orden')
    ideasfuerza_a = IdeaFuerza.objects.filter(seccion='a').order_by('orden')
    citas = Cita.objects.order_by('orden')
    candidatos = Candidato.objects.order_by('orden')
    documentos = Documento.objects.order_by('orden')
    return render(request, 'index.html', {
        'ideasfuerza_m': ideasfuerza_m,
        'ideasfuerza_p': ideasfuerza_p,
        'ideasfuerza_a': ideasfuerza_a,
        'citas': citas,
        'candidatos': candidatos,
        'documentos': documentos,
    })
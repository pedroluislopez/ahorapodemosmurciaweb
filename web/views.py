from django.shortcuts import render
from web.models import Candidato

# Create your views here.
# Create your views here.
def index(request):
    candidatos = Candidato.objects.order_by('orden')
    return render(request, 'index.html', {'candidatos': candidatos})
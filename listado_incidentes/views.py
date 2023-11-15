from django.shortcuts import render
from listado_incidentes.models import Incidente
from rest_framework.decorators import api_view


@api_view(['GET'])
def lista_de_incidenes(request):
    incidentes = Incidente.objects.all()
    return render(request, 'incident_list.html', {'incidentes': incidentes})

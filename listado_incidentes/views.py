from django.shortcuts import render
from listado_incidentes.models import Incident
from rest_framework.decorators import api_view


@api_view(['GET'])
def incident_list(request):
    incidents = Incident.objects.all()
    return render(request, 'incident_list.html', {'incidents': incidents})

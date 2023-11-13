from django.shortcuts import render
from listado_incidentes.models import Incident


# Create your views here.
def incident_list(request):
    incidents = Incident.objects.all()
    return render(request, 'incident_list.html', {'incidents': incidents})

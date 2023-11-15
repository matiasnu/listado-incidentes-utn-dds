from django.db import models


# Create your models here.
class Incidente(models.Model):
    class Meta:
        db_table = "incidente"

    detalle = models.CharField(max_length=200)
    fecha_apertura = models.DateTimeField(auto_now_add=True)

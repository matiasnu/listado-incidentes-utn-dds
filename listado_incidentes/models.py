from django.db import models


# Create your models here.
class Incident(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)

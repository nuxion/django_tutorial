from django.db import models

# Create your models here.
# object relational mapper f

class Curso(models.Model):

    nombre = models.CharField(max_length=128)
    inscriptos = models.IntegerField()
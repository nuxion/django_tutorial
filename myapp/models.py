from django.db import models

# Create your models here.
# object relational mapper f

class Profesor(models.Model):
    nombre = models.CharField(max_length=128)
    monotributista = models.BooleanField()

    

class Curso(models.Model):

    nombre = models.CharField(max_length=128)
    inscriptos = models.IntegerField()

    TURNOS = (
        (1, "Manana"),
        (2, "Tarde"),
        (3, "Noche"),

    )
    turnos = models.PositiveSmallIntegerField(choices=TURNOS)

    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, related_name="cursos")


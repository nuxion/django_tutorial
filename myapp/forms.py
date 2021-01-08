from django import forms
from myapp.models import Curso

class FormularioCurso(forms.ModelForm):

    class Meta:
        model = Curso
        fields = ("nombre", "inscriptos", "turnos")

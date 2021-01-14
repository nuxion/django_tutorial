#from django.shortcuts import render
#from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, Http404
from myapp.models import Curso, Profesor
from django.urls import reverse
from myapp import forms 
from django.views import generic
import logging

log = logging.getLogger(__name__)

# Create your views here.
def index(request):

    log.error("Desde mi logger")
    msg = "Hola mundo"
    agent = request.headers['User-Agent']
    cursos = Curso.objects.all()




    data = {
        'agent': agent,
        'asignados': 2,
        'cursos': cursos,
        'alumno': { 'name': 'Xavier', 'lastname': 'Petit'}
    }

    
    return render(request, 'index.html', context=data)



def about(request, name=None):

    return render(request, 'about.html', context={'name': name})


def cursos_one(request, name=None):
    try:
        one = Curso.objects.get(nombre=name)
    except Curso.DoesNotExist:
        return JsonResponse({'msg': "no existe"}, status=404)


    if request.method == "DELETE":
        one.delete()
        return JsonResponse({'msg': f'{one.nombre} delted'}, safe=False)

    return JsonResponse({'nombre': one.nombre, 'inscriptos': one.inscriptos}, safe=False)


def cursos_all(request, name=None):
    if request.method == "POST":
        nombre = request.POST['nombre']
        inscriptos = int(request.POST['inscriptos'])
        curso = Curso.objects.create(nombre=nombre, inscriptos=inscriptos)
        return JsonResponse({ 'msg': curso.id}, status=201)
    

    return JsonResponse(list(Curso.objects.all().values()), safe=False)


def nuevo_curso(request):

    if request.method == "POST":
        form = forms.FormularioCurso(request.POST)
        if form.is_valid():
            #Curso.objects.create(
            #    nombre=form.cleaned_data["nombre"],
            #    inscriptos=form.cleaned_data["inscriptos"],
            #)
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = forms.FormularioCurso()

    ctx = {'form': form}

    return render(request, 'nuevo_curso.html', ctx)



class CursoGeneric(generic.ListView):
    template_name = 'cursos.html'
    context_object_name = 'cursos'

    def get_queryset(self):
        """Return the last five published questions."""
        return Curso.objects.order_by('turnos')[:5]



#from django.shortcuts import render
#from django.http import HttpResponse
# from django.http import JsonResponse
from django.shortcuts import render
from myapp.models import Curso

# Create your views here.
def index(request):


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

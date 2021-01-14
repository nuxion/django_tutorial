from django.contrib import admin

# Register your models here.

from myapp.models import Curso, Profesor


class CursoAdmin(admin.ModelAdmin):

    fields = ['nombre', 'turnos', 'profesor']
    list_filter = ['turnos', 'profesor']
    search_fields = ['nombre']


admin.site.register(Curso, CursoAdmin)
admin.site.register(Profesor)

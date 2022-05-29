from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def saludo(request, nombre):
    return HttpResponse(f'Buenas tardes {nombre}')

def probandoTemplate(request):
    context = {
        'nombre' : 'Mateo',
        'apellido' : 'Ingouville',
        'edades' : [10, 18, 22, 44, 60],
        'fecha' : datetime.now()
    }
    return render(request, 'template1.html', context = context)

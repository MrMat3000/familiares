from django.shortcuts import render
from familiares.models import Familiares

# Create your views here.
def familiares(request):
    context = {}
    return render(request, 'familiares.html', context = context)
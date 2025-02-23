from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):

    #name = "Manmohan"

    context = {
        'name': 'Manmohan',
        'age': 22
    }   
    return render(request, 'index.html', context )



from django.shortcuts import render
from .models import Portafolio

def portafolio(request):

    portafolio = Portafolio.objects.all()

    return render(request, "portafolio.html", {
        'title':'Portafolio' ,
        'portafolio': portafolio
    })
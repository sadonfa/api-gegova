from django.shortcuts import render
from .models import About

# Create your views here.

def about(request):

    about = About.objects.all()

    return render(request, "about.html", {
        "title": "About",
        "abouts": about
    })
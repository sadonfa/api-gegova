from django.shortcuts import render

# Create your views here.

def curriculum(request):
    return render(request, "curriculum.html", {
        'title': 'Curriculum'
    })
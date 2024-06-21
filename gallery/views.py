from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from .models import Client, ImageClie

# Create your views here.

def gallery(request):

    client = Client.objects.all()

    paginator = Paginator(client, 3)

    page = request.GET.get('page')
    page_client = paginator.get_page(page)

    return render(request, "gallery.html", {
        "title" : "Galeria",
        "clients": page_client
    })

def add_client(request):

    return render(request, "add_client.html", {
        "title": "Agregar un cliente",
    })

def save_client(request):

    if request == 'POST':

        name = request.POST['name']
        image = request.FILES['image']   

        cliente = Client(
            name = name,
            image = image
        )

        print(cliente)
        cliente.save()

        return HttpResponse(f"cliente creado: <strong>{cliente.name}</strong> ")
    else:
        return HttpResponse("No se a resivido datos por GET")


def gall_client(request, category):

    img_client = ImageClie.objects.filter(category=category)
    # img_client = ImageClie.objects.all()

    # print("ESTO ES LO QUE RECOJO DE PARAMETRO " + img_client)
    return render(request, "client.html",{
        "title" : "Cliente",
        "galleries": img_client
    })
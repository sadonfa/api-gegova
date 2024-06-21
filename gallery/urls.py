from django.urls import path
from . import views

urlpatterns = [
    path('gallery/', views.gallery, name="gallery" ),
    path('client/<int:category>/', views.gall_client, name="client"),
    path('add-client/', views.add_client, name="add-client"),
    path('save-client/', views.save_client, name="save_client")
]

from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    image = models.ImageField(default="null", upload_to="Client", verbose_name="Imagen")
    create_ad = models.DateTimeField(auto_now_add=True, verbose_name="Creado el ")
    update_ad = models.DateTimeField(auto_now=True, verbose_name="Actualizado el ")
    
    def __str__(self):
        return f'{self.name}'

class ImageClie(models.Model): 
    name = models.CharField(max_length=200, verbose_name="Nombre")
    image = models.ImageField(default="null", upload_to="ImageClie", verbose_name="Imagen" )
    category = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Categoria")
    create_ad = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    update_ad = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    def __str__(self):
        return f'{self.name}'
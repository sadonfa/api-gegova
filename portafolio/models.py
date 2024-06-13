from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre" )
    description = models.CharField(max_length=200, verbose_name="Descripcion")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

class Lenguajes(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre" )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Lenguaje"
        verbose_name_plural = "Lenguajes"

    def __str__(self):
        return self.name

class Portafolio(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE , verbose_name="Categoria")
    lenguajes = models.ManyToManyField(Lenguajes, blank=True, verbose_name="Lenguaje")
    image = models.ImageField(default="null", upload_to="Imagen")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Portafolio"
        verbose_name_plural = "Portafolios"

    def __str__(self):
        return self.name
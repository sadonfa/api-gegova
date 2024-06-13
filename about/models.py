from django.db import models
# from ckeditor.fields import RichTextField
# from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    info = models.TextField(verbose_name="info")
    icono = models.CharField(
        max_length=50, default="none", verbose_name="Icono")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"

    def __str__(self):
        return self.title


# class Page(models.Model):
#     title = models.CharField(max_length=50, verbose_name="Titulo")
#     content = RichTextField(verbose_name="Contenido")
#     slug = models.CharField(unique=True, max_length=150,
#                             verbose_name="URL amigable")
#     order = models.IntegerField(default=0, verbose_name='Orden')
#     visible = models.BooleanField(verbose_name="¿Visible?")
#     created_at = models.DateTimeField(
#         auto_now_add=True, verbose_name="Creado el")
#     updated_at = models.DateTimeField(
#         auto_now=True, verbose_name="Actualizado el")

#     class Meta:
#         verbose_name = "Pagina"
#         verbose_name_plural = "Paginas"

#     def __str__(self):
#         return self.title

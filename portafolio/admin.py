from django.contrib import admin
from .models import Categories, Lenguajes, Portafolio

class CategoriesAdmin(admin.ModelAdmin):

    # add the fields of the model here
    list_display = ("name", "description", "created_at", "updated_at")
    readonly_fields = ( 'created_at', 'updated_at')

class LenguajesAdmin(admin.ModelAdmin):

    # add the fields of the model here
    list_display = ("name", "created_at", "updated_at")
    readonly_fields = ( 'created_at', 'updated_at')


class PortafoliaAdmin(admin.ModelAdmin):

    # add the fields of the model here
    list_display = ("name", "created_at", "updated_at")
    readonly_fields = ( 'created_at', 'updated_at')



# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(Portafolio, PortafoliaAdmin )
admin.site.register(Categories, CategoriesAdmin )
admin.site.register(Lenguajes, LenguajesAdmin)

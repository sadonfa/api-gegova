from django.contrib import admin

# import the model Todo
from .models import About

# create a class for the admin-model integration


class AboutAdmin(admin.ModelAdmin):

    # add the fields of the model here
    list_display = ("title", "info", "icono")
    readonly_fields = ( 'created_at', 'updated_at')


# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(About, AboutAdmin)

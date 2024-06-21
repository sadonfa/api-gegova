from django.contrib import admin
from .models import Client, ImageClie

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display =  ('name', 'image', 'create_ad', 'update_ad')

class ImageClieAdmin(admin.ModelAdmin):
    list_display =  ('name', 'image', 'create_ad', 'update_ad')


admin.site.register(Client, ClientAdmin)
admin.site.register(ImageClie, ImageClieAdmin)
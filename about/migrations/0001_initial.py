# Generated by Django 5.0.6 on 2024-06-05 05:30

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('info', django_ckeditor_5.fields.CKEditor5Field(verbose_name='info')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Pagina',
                'verbose_name_plural': 'Paginas',
            },
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-08 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portafolio',
            name='lenguajes',
        ),
        migrations.AddField(
            model_name='portafolio',
            name='lenguajes',
            field=models.ManyToManyField(blank=True, to='portafolio.lenguajes', verbose_name='Lenguaje'),
        ),
    ]

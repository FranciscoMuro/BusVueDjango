# Generated by Django 4.0.4 on 2022-04-20 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trayectos', '0002_remove_trayecto_fecha_hora_salida_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trayecto',
            name='choferId',
        ),
        migrations.RemoveField(
            model_name='trayecto',
            name='fecha_salida',
        ),
        migrations.RemoveField(
            model_name='trayecto',
            name='hora_salida',
        ),
    ]

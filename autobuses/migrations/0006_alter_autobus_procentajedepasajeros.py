# Generated by Django 4.0.4 on 2022-04-28 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autobuses', '0005_alter_autobus_procentajedepasajeros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autobus',
            name='procentajeDePasajeros',
            field=models.IntegerField(default=0, max_length=3, verbose_name='Porcentaje de pasajeros por autobus'),
        ),
    ]

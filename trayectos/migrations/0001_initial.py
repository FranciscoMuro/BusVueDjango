# Generated by Django 4.0.4 on 2022-04-18 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('choferes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trayecto',
            fields=[
                ('trayectoId', models.AutoField(primary_key=True, serialize=False)),
                ('origen', models.CharField(max_length=50, verbose_name='ubicacion de partida del viaje')),
                ('destino', models.CharField(max_length=50, verbose_name='ubicacion de llegada del viaje')),
                ('fecha_hora_salida', models.DateField()),
                ('choferId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='choferes.chofer', verbose_name='Chofer del autobus')),
            ],
        ),
    ]

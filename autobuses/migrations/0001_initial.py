# Generated by Django 4.0.4 on 2022-04-18 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('choferes', '0001_initial'),
        ('trayectos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autobus',
            fields=[
                ('busId', models.AutoField(primary_key=True, serialize=False)),
                ('Chofer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='choferes.chofer', verbose_name='Chofer del autobus')),
                ('trayecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trayectos.trayecto', verbose_name='Chofer del autobus')),
            ],
        ),
    ]
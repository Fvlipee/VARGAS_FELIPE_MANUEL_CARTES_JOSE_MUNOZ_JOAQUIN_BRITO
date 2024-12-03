# Generated by Django 3.1.2 on 2024-10-18 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20241018_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariopersonalizado',
            name='actividades',
            field=models.ManyToManyField(blank=True, to='core.Actividad'),
        ),
        migrations.AddField(
            model_name='usuariopersonalizado',
            name='tareas',
            field=models.ManyToManyField(blank=True, to='core.Tarea'),
        ),
    ]

# Generated by Django 3.1.2 on 2024-10-18 02:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20241017_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='fecha_creacion',
        ),
        migrations.AddField(
            model_name='tarea',
            name='asignada_a',
            field=models.ManyToManyField(related_name='tareas_asignadas', to=settings.AUTH_USER_MODEL),
        ),
    ]

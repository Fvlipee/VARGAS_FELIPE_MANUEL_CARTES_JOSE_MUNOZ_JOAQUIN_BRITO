# Generated by Django 3.1.2 on 2024-10-21 00:50

from django.db import migrations

from django.db import migrations

def create_initial_activities(apps, schema_editor):
    Actividad = apps.get_model('core', 'Actividad')

    # Crear actividades predefinidas
    actividad1 = Actividad(
        titulo='ANALISIS DE CONDUCTA (ACC)',
        descripcion='Realizar un análisis detallado de la conducta.',
        imagen_url='ruta/a/la/imagen_acc.jpg'
    )
    actividad1.save()

    actividad2 = Actividad(
        titulo='Reflexión diaria: ¿Cómo estuvo tu día?',
        descripcion='Escribe una reflexión sobre cómo estuvo tu día.',
        imagen_url='ruta/a/la/imagen_reflexion.jpg'
    )
    actividad2.save()

    actividad3 = Actividad(
        titulo='Dibujo y Descripción',
        descripcion='Dibuja una escena y luego descríbela en detalle.',
        imagen_url='ruta/a/la/imagen_dibujo.jpg'
    )
    actividad3.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '000X_previous_migration'),  # Reemplaza con la última migración anterior
    ]

    operations = [
        migrations.RunPython(create_initial_activities),
    ]


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_tareaasignada_completada'),
    ]

    operations = [
    ]
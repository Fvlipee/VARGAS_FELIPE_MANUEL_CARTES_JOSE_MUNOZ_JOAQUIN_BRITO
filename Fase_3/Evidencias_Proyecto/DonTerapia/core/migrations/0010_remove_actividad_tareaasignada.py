# Generated by Django 3.1.2 on 2024-10-18 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20241018_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad',
            name='tareaasignada',
        ),
    ]
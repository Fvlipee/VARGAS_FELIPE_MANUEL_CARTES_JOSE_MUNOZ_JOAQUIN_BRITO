# Generated by Django 3.1.2 on 2024-10-24 03:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuestatarea',
            name='fecha_realizacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
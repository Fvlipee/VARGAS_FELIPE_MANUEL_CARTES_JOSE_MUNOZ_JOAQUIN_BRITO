# Generated by Django 3.1.2 on 2024-10-18 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20241018_0104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad',
            name='tareas_asignadas',
        ),
        migrations.RemoveField(
            model_name='actividadrealizada',
            name='antecedentes',
        ),
        migrations.RemoveField(
            model_name='actividadrealizada',
            name='conducta',
        ),
        migrations.RemoveField(
            model_name='actividadrealizada',
            name='consecuencia',
        ),
        migrations.RemoveField(
            model_name='actividadrealizada',
            name='fecha_hora',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='actividades',
        ),
        migrations.RemoveField(
            model_name='usuariopersonalizado',
            name='tareas',
        ),
        migrations.AddField(
            model_name='tarea',
            name='completada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='imagen_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='respuestatarea',
            name='tarea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuestas', to='core.tarea'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='actividad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to='core.actividad'),
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='asignada_a',
        ),
        migrations.AddField(
            model_name='tarea',
            name='asignada_a',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tareas_asignadas', to='core.usuariopersonalizado'),
            preserve_default=False,
        ),
    ]

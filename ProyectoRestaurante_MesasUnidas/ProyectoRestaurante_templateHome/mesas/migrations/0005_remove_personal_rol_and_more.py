# Generated by Django 5.1.4 on 2025-02-02 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mesas', '0004_remove_mesa_identificador_mesa_cantidad_uso_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='rol',
        ),
        migrations.AlterField(
            model_name='personal',
            name='identificador_Personal',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]

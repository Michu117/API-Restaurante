# Generated by Django 5.1.4 on 2025-02-02 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0011_alter_receta_cantidad_necesaria'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historialpedido',
            options={'verbose_name_plural': 'Historial de Pedidos'},
        ),
    ]

# Generated by Django 5.1.5 on 2025-02-01 19:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mesas', '0003_alter_reserva_cliente'),
        ('pedidos', '0005_remove_pedido_reservacion_pedido_reserva_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='mesa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mesas.mesa', verbose_name='Mesa'),
        ),
        migrations.DeleteModel(
            name='Mesa',
        ),
    ]

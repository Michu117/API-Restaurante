# Generated by Django 5.1.5 on 2025-02-01 19:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mesas', '0003_alter_reserva_cliente'),
        ('pedidos', '0004_alter_detallepedido_producto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='reservacion',
        ),
        migrations.AddField(
            model_name='pedido',
            name='reserva',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mesas.reserva', verbose_name='Reservación'),
        ),
        migrations.DeleteModel(
            name='Reservacion',
        ),
    ]

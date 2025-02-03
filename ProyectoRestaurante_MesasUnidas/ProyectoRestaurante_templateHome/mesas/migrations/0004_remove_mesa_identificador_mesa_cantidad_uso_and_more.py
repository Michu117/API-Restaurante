# Generated by Django 5.1.5 on 2025-02-01 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mesas', '0003_alter_reserva_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mesa',
            name='identificador',
        ),
        migrations.AddField(
            model_name='mesa',
            name='cantidad_uso',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mesa',
            name='codigo',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]

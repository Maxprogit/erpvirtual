# Generated by Django 2.1.15 on 2023-11-29 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20231127_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='Cantidad',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='Telefono',
            field=models.CharField(max_length=100),
        ),
    ]
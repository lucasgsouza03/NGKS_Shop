# Generated by Django 2.0.6 on 2018-11-04 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0005_estoque_materia_prima_estoque_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque_materia_prima',
            name='quantidade',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='estoque_produto',
            name='quantidade',
            field=models.BigIntegerField(default=0),
        ),
    ]

# Generated by Django 2.0.6 on 2019-10-03 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_auto_20191003_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoque_materia_prima',
            name='watermark',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='estoque_produto',
            name='watermark',
            field=models.IntegerField(null=True),
        ),
    ]

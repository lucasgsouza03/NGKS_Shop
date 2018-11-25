# Generated by Django 2.0.6 on 2018-11-25 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='altura',
            field=models.FloatField(default=1, verbose_name='Altura'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='comprimento',
            field=models.FloatField(default=1, verbose_name='Comprimento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='diamentro',
            field=models.IntegerField(default=1, verbose_name='Diametro'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='peso',
            field=models.FloatField(default=1, verbose_name='Peso'),
            preserve_default=False,
        ),
    ]

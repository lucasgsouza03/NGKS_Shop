# Generated by Django 2.0.6 on 2018-11-04 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0011_auto_20181104_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='produtos', verbose_name='Imagem'),
        ),
    ]
# Generated by Django 2.0.6 on 2018-06-25 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGU', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='validacao',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
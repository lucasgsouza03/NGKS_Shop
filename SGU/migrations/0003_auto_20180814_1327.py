# Generated by Django 2.0.6 on 2018-08-14 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SGU', '0002_usuario_validacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='ativo',
            new_name='is_active',
        ),
    ]

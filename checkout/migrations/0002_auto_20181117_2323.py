# Generated by Django 2.0.6 on 2018-11-18 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='opcao_pagamento',
            field=models.CharField(choices=[('pagseguro', 'Pagseguro'), ('paypal', 'Paypal')], max_length=20, verbose_name='Opação de Pagamento'),
        ),
    ]
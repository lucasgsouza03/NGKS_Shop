# Generated by Django 2.0.6 on 2018-11-04 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0013_auto_20181104_0408'),
        ('estoque', '0004_auto_20181019_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='estoque_materia_prima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('cor', models.CharField(max_length=100, verbose_name='Cor')),
                ('tamanho', models.CharField(max_length=100, verbose_name='Tamanho')),
                ('quantidade', models.BigIntegerField()),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.fornecedor')),
                ('materia_prima', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Materia', verbose_name='Matéria Prima')),
            ],
        ),
        migrations.CreateModel(
            name='estoque_produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='produtos', verbose_name='Imagem')),
                ('cor', models.CharField(max_length=100, verbose_name='Cor')),
                ('tamanho', models.CharField(max_length=100, verbose_name='Tamanho')),
                ('quantidade', models.BigIntegerField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Produto', verbose_name='Produto')),
            ],
        ),
    ]
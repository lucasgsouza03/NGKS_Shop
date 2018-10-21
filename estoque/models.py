from django.db import models
from catalogo.models import Produto
from django.urls import reverse
# Create your models here.

class fornecedor(models.Model):
    nome = models.CharField('Fornecedor', max_length=100)
    slug = models.SlugField('Identificador', max_length=100, default='forn')
    tipo = models.CharField('Tipo de fornecedor', max_length=100)
    cnpj = models.BigIntegerField('CNPJ')
    email = models.CharField('E-mail',max_length=100, unique=True)
    telefone = models.IntegerField('Telefone')

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('estoque:fornecedor_detalhes', kwargs={'slug':self.slug}) 
'''
class estoque_produto(models.Model):
    produto = models.ForeignKey('catalogo.Produto', verbose_name='Produto', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
'''
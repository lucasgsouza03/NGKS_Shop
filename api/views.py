from django.shortcuts import render
from rest_framework import viewsets
from estoque.models import estoque_produto
from .serializers import estoqueProdutoSerializer


class estoqueProdutoViewSet(viewsets.ModelViewSet):
    queryset = estoque_produto.objects.all()
    serializer_class = estoqueProdutoSerializer

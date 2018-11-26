from catalogo.models import Categoria
from checkout.models import CartItem

def categorias(request):
    return {
        'categorias': Categoria.objects.all() 
    }

def carrinho(request):
    total = 0
    quantidade = 0
    session_key = request.session.session_key
    itens = CartItem.objects.filter(cart_key=session_key)
    for i in itens:
        valor = i.preco * i.quantidade
        total = total + valor
        quantidade = quantidade + i.quantidade

     
    return {
        'itens': itens,
        'total': total,
        'quantidade': quantidade
    }    
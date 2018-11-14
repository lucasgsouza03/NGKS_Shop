from django.db import models
from django.conf import settings

# Create your models here.

class CartItemManager(models.Manager):

    def add_item(self, cart_key, produto):
        if self.filter(cart_key=cart_key, produto=produto).exists():
            created = False
            cart_item = self.get(cart_key=cart_key, produto=produto)
            cart_item.quantidade = cart_item.quantidade + 1
            cart_item.save()
        else:
            created = True
            cart_item = CartItem.objects.create(cart_key=cart_key, produto=produto, preco=produto.price)
                  
        return cart_item, created

class CartItem(models.Model):

    cart_key = models.CharField('Chave do Carrinho', max_length=40, db_index=True)
    quantidade = models.PositiveIntegerField('Quantidade', default=1)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    produto = models.ForeignKey(
        'catalogo.produto',
        on_delete=models.DO_NOTHING,
        verbose_name='catalogo.produto'
    )

    objects = CartItemManager()

    class Meta:
        verbose_name = 'Item do Carrinho'
        verbose_name_plural = 'Itens dos Carrinhos'
        unique_together = (('cart_key', 'produto'),)


    def __str__(self):
        return '{} [{}]'.format(self.produto, self.quantidade)

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens dos pedidos'

    def __str__(self):
        return '[{}] {}'.format(self.order, self.produto)


def post_save_cart_item(instance, **kwargs):
    if instance.quantidade < 1:
        instance.delete()

models.signals.post_save.connect(
    post_save_cart_item, sender=CartItem, dispatch_uid='post_save_cart_item')

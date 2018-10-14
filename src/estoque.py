from estoque.models import fornecedor

class Gerencia_fornecedor():

    def Deleta_fornecedor(delete):
        fornecedor.objects.get(id=delete).delete()
    
    def Atualiza_fornecedor(request, slug):
        nome = request.POST.get("nome")
        tipo = request.POST.get("tipo")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")

        forn = fornecedor.objects.get(slug=slug)
        forn.nome = nome
        forn.tipo = tipo
        forn.email = email
        forn.telefone = telefone
        forn.save()
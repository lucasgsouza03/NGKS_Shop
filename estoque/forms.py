from django import forms
from .models import fornecedor

class cadastrar_fornecedor(forms.ModelForm):
    class Meta:
        model = fornecedor
        fields = ['nome', 'tipo', 'cnpj', 'email', 'telefone']

    def save(self, commit=True):
        this = super(cadastrar_fornecedor, self).save(commit=False)
        this.slug = this.nome
        if commit:
            this.save()
        return this
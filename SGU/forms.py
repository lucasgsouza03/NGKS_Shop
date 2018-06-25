from django import forms
from django.forms import ModelForm
from SGU.models import usuario

class cadasto_user(ModelForm):
    class Meta():
        model = usuario
        fields = ['username','password', 'nome', 'email']

    def save(self, commit=True):
        user = super(cadasto_user, self).save(commit=False)
        user.set_password(user.password)
        if commit:
            user.save()
        return user


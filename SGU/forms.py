from django import forms
from django.forms import ModelForm
from SGU.models import Usuario

class form_usuario(ModelForm):
    class Meta():
        model = Usuario
        fields = ['username','password', 'nome', 'email']

    def save(self, commit=True):
        user = super(form_usuario, self).save(commit=False)
        user.set_password(user.password)
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(label=(u'Username'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
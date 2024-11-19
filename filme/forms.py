# CRIANDO O FORMULÁRIO DE CRIAÇÃO DE CONTAS

# Importando biblioteca(s)
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms



# Definindo a classe FormHomepage usando o modelo de formulário Padrão do Django
class FormHomepage(forms.Form):
    # No formulário padrão tem somente o campo de email
    email = forms.EmailField(label=False)



# Definindo a classe CriarContaForm como sendo uma subclasse do UserCreationForm
# Obs.: utilizaremos um modelo próprio (personalizado) pois será incluído o campo de e-mail
class CriarContaForm(UserCreationForm):
    # Edição 01: Criando o campo de e-mail como obrigatório
    email = forms.EmailField()
    # Definindo a classe Meta (é assim que o Django pede para fazer)
    class Meta:
        # Definindo o modelo que gerencia o usuário (modelo Padrão do Django ou modelo Próprio?)
        model = Usuario
        # Edição 02: Uma Tupla que vai dizer quais serão os campos a serem exibidos no Formulário
        fields = ('username', 'email', 'password1', 'password2')





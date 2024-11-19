from django.contrib import admin

# Importando as classes Filme, Episodio e Usuario (as tabelas do APP) que foram criadas em models.py
from .models import Filme, Episodio, Usuario

# Importando a classe que irá gerenciar os usuários (Login, Logout, as secções abertas pelo usuário, fechamento e nova abertura do navegador)
from django.contrib.auth.admin import UserAdmin


# Este trecho somente é necessário se eu desejar que no Admin seja exibido o campo personalizado filmes_vistos
# Obs.: somente aparecerá no Admin se for adicionado manualmente da maneira abaixo
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico de Filmes Vistos pelo Usuário", {"fields": ("filmes_vistos", )})
)
UserAdmin.fieldsets = tuple(campos)



# Register your models here.

# Registrando o APP Filme
admin.site.register(Filme)

# Registrando o APP Episodio
admin.site.register(Episodio)

# Registrando o APP Usuario
admin.site.register(Usuario, UserAdmin)




# Importando biblioteca(s)
from .models import Filme

# Criando gerenciadores de contexto que funcionam para todas as Views

# Definindo uma Gerenciador de Contexto para a Lista de Filmes Recentes
def lista_filmes_recentes(request):
    #
    lista_filmes = Filme.objects.all().order_by("-data_criacao")[0:8]
    
    # Alternativa à criação ao Gerenciador de Contexto filme_destaque, vide abaixo
    if lista_filmes:
        filme_destaque = lista_filmes[0]
    else:
        filme_destaque = None
    
    # Retornando a chave do dicionário que será utilizada no arquivo Html
    return {"lista_filmes_recentes": lista_filmes, "filme_destaque": filme_destaque}


# Definindo uma Gerenciador de Contexto para a Lista de Filmes Em Alta
def lista_filmes_emalta (request):
    lista_filmes = Filme.objects.all().order_by("-visualizacoes")[0:8]
    # Retornando a chave do dicionário que será utilizada no arquivo Html
    return {"lista_filmes_emalta": lista_filmes}

# Definindo uma Gerenciador de Contexto para a Lista de Filmes Em Destaque
# Obs.1: comentada a linha 'filme.new_context.filme_destaque', em settings.py 
# Obs.2: comentado trecho abaixo
# def filme_destaque(request):
#     filme = Filme.objects.order_by("-data_criacao")[0]
#     return {"filme_destaque": filme}


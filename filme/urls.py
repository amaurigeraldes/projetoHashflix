# CRIANDO A URL DA PÁGINA FILME

# Importando biblioteca(s)
from django.urls import path, reverse_lazy
# from .views import homepage, homefilmes # Usando a FBV
from .views import Homefilmes, Homepage, Detalhesfilme, Pesquisa_filme, Paginaperfil, Criarconta # Usando a CBV

# Importando a View Padrão para autenticação como auth_view
from django.contrib.auth import views as auth_view


# Definindo um app_name
# Obs.: é melhor que o app_name tenha o mesmo nome do App
app_name = "filme"


# Criando os Padrões dos Links da Página
urlpatterns = [
    # Fazendo o link com a 
    # Obs.1: deixando vazio, '' para gerenciar todos os links do site, porém, se criarmos mais páginas, essa informação deverá preenchida, para ser definido qual o link deverá ser acessado, pois não pode haver duas ou mais páginas com a mesma URL
    # Obs.2: incluindo a view homepage (função criada em views.py)
    # path('', homepage), # Usando a FBV
    # path('filmes/', homefilmes), # Usando a FBV
    path('', Homepage.as_view(), name="homepage"), # Usando a CBV
    path('filmes/', Homefilmes.as_view(), name="homefilmes"), # Usando a CBV
    # Usando <int:pk> para passar a Primary Key do Modelo da Classe Detalhesfilme.as_view() que é um filme
    # Obs.: a pk (Primary Key) é o Id do Item (Filme) criado automaticamente pelo Django no Banco de Dados
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name="detalhesfilme"),
    path('pesquisa/', Pesquisa_filme.as_view(), name="pesquisa_filme"),
    path('login/', auth_view.LoginView.as_view(template_name = "login.html"), name="login"),
    # Usando <int:pk> para passar a Primary Key do Modelo da Classe Detalhesfilme.as_view() que é um filme
    # Obs.: a pk (Primary Key) é o Id do Usuário criado automaticamente pelo Django no Banco de Dados
    path('logout/', auth_view.LogoutView.as_view(template_name = "logout.html"), name="logout"),
    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name="editarperfil"),
    path('criarconta/', Criarconta.as_view(), name="criarconta"), 
    # Usando o auth_view.PasswordChangeView.as_view() criar a URL para mudança da senha
    # Obs.1: passando como parâmetro template_name = "editarperfil.html" para não ser necessária a criação de uma Nova Página Html igual
    # Obs.2: passando como parâmetro success_url = reverse_lazy('filme:homefilmes') para não ser necessário definir no settings.py
    # Obs.3: importar a biblioteca reverse_lazy
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name = "editarperfil.html", 
                                                             success_url = reverse_lazy('filme:homefilmes')), name="mudarsenha"),
]
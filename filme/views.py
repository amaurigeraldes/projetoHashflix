# Importando biblioteca(s)
from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from .forms import CriarContaForm, FormHomepage

# Importando a classe TemplateView, pois o único objetivo da página homepage.html é exibir um Template
# Obs.: existem outras classes prontas do Django, por exemplo, CreateView, ListView, DetailView, FormView, UpdateView
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView

# Importando uma classe que pode ser passada e que permite bloquear as CBV
# Obs.: o LoginRequiredMixin precisa ser o primeiro parâmetro a ser passado
from django.contrib.auth.mixins import LoginRequiredMixin   


# Create your views here.

# PARA A CRIAÇÃO DE UMA NOVA VIEW, OU SEJA, UMA PÁGINA NOVA NO SITE, DEVERÁ TER OBRIGATÓRIAMENTE UMA URL, UMA VIEW E UM TEMPLATE (Página HTML)

# =============================== Podemos criar Views de 2 Formas: =====================================
# 1) Criando uma Function (FBV), usando a forma padrão do Python de programar, criar e usar funções para puxar a lista de views
# Vantagens: mais simples de criar, mais fácil de começar, sendo mais prática para Sites Mais Simples
# Desvantagens: você tem que criar todos os processo e criar a lista de itens

# 2) Criando uma Class (CBV), ou seja, uma Classe que irá gerenciar a View, programando as views usando Programação Orientada a Objeto (Herança de uma Classe Padrão do Django), listando os elementos criados no Models
# Vantagens: em diferentes sites do Django vão querer criar Views que são Views de Lista de Itens, sendo uma página de detalhes específicos de um item do nosso modelo
# Desvantagens: já vai trazer muitas coisas prontas, mas você precisa saber qual classe terá que usar para trazer a coisas prontas que você precisa, é mais difícil e mais confuso num primeiro momento
# ======================================================================================================

# FORMA 01 - CRIAÇÃO DE UMA FBV 
# Criando a função homepage e passando por padrão o parâmetro request que faz uma Requisição para o Site
# Obs.1: a requisição do tipo GET é quando você pesquisa um site a partir do seu navegador (vendo um site)
# Obs.2: a requisição do tipo POST é quando você preenche uma formulário e clica em enviar (enviando uma informação)
# def homepage(request): # Linha Comentada
    # Fazendo o return, usando o render para renderizar a página e passando os parâmetros, request (requisição GET ou POST) e o template homepage.html
    # return render(request, "homepage.html") # Linha Comentada

# FORMA 02 - CRIAÇÃO DE UMA CBV (Fazendo as adaptações para a criação de uma Classe)
# Obs.: fazer a importação da biblioteca FormView
class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomepage

    def get(self, request, *args, **kwargs):
        # Se o usuário estiver autenticado
        if request.user.is_authenticated:
            # Redirecionando o Usuário para uma outra View, a homefilmes
            # Obs.1: importar a biblioteca redirect
            # Obs.2: passando como parâmetro 'filme:homefilmes', onde filme é o app_name e homefilmes é o name definido em urls.py
            return redirect('filme:homefilmes')
        # Caso contrário
        else:
            # Redirecionando o Usuário para a URL Final, no caso a homepage.html caso o usuário não esteja autenticado
            return super().get(request, *args, **kwargs)
        
    # Definindo a função obrigatória sempre que for criada uma FormView, para o caso de o Formulário ser bem sucedido
    def get_success_url(self):
        email = self.request.POST.get('email')
        usuarios = Usuario.objects.filter(email = email)
        if usuarios:
            # Usando o reverse() para retornar um texto de Link como resposta, para onde o usuário será direcionado
            # Obs.1: importar a biblioteca reverse
            # Obs.2: não pode ser um redirect('filme:login') pois não é um Link, precisa ser um texto de Link que corresponde ao Link do 'filme:login'
            return reverse('filme:login')
        else:
            # Usando o reverse() para retornar um texto de Link como resposta, para onde o usuário será direcionado
            # Obs.1: importar a biblioteca reverse
            # Obs.2: não pode ser um redirect('filme:criarconta') pois não é um Link, precisa ser um texto de Link que corresponde ao Link do 'filme:criarconta'
            return reverse('filme:criarconta')
    
    


# FORMA 01 - CRIAÇÃO DE UMA FBV 
# Criando a function homefilmes
# def homefilmes(request): # Linha Comentada
    # Usando um Context (Dicionário Python) para passar uma Lista com todos os filmes para a View
    # context = {} # Linha Comentada
    # Criando uma Lista com todos os filmes do Banco de Dados e atribuindo a uma variável
    # lista_filmes = Filme.objects.all() # Linha Comentada
    # Criando uma Chave no Dicionário para a Lista de Filmes
    # context['lista_filmes'] = lista_filmes # Linha Comentada
    # Passando a variável Context como sendo o Terceiro Parâmetro
    # return render (request, "homefilmes.html", context) # Linha Comentada

# FORMA 02 - CRIAÇÃO DE UMA CBV (Fazendo as adaptações para a criação de uma Classe)
# Obs.1: a função é a exibição de uma Lista de Filmes (uma lista de objetos do banco de dados), portanto, fazer a importação da biblioteca ListView
# Obs.2: passando o parâmetro LoginRequiredMixin para que o usuário tenha que fazer obrigatóriamente o login para acessar a página
class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    # Definindo o Modelo do Banco de Dados, o Contexto, puxa a Lista de Filmes e passa para o arquivo HTML como sendo uma object_list (passar para o homefilmes.html em substituição a lista_filmes)
    model = Filme
    # object_list -> lista de itens do modelo

# Definindo uma classe para exibir os Detalhes do Filme
# Obs.: passando o parâmetro LoginRequiredMixin para que o usuário tenha que fazer obrigatóriamente o login para acessar a página
class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    # Definindo o Modelo do Banco de Dados, o Contexto, puxa a Lista de Filmes e passa para o arquivo HTML como sendo uma object_list (passar para o homefilmes.html em substituição a lista_filmes)
    model = Filme
    # object -> 1 item do modelo
    
    def get(self, request, *args, **kwargs):
        # Descobrindo qual filme o usuário está acessando e editando um campo do Banco de Dados dentro da View
        filme = self.get_object()
        # Contabilizando a exibição do filme (somando 1 nas visualizações do filme)
        filme.visualizacoes += 1
        #  Salvando as visualizações
        filme.save()
        # Atribuindo a variávek usuario uma request.user
        usuario = request.user
        # Usando o método add() para adicionar um item a um campo do Banco de Dados
        usuario.filmes_vistos.add(filme)
        # Redirecionando o Usuário para a URL Final, no caso a detalhesfilme.html
        return super().get(request, *args, **kwargs)
        
    
    
    # Criando um context para a View de Filmes Relacionados
    # Obs.: esta View funciona somente para a View Detalhesfilme
    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        # filtrando a minha tabela de filmes pegando os filmes cuja categoria é igual a categoria do filme da página (object)
        # Obs.: Filme poderia ser substituído por self.model
        filmes_relacionados = Filme.objects.filter(categoria = self.get_object().categoria)[0:5 ]
        context["filmes_relacionados"] = filmes_relacionados
        return context
    

# Definindo a classe Pesquisa_filme e usando uma ListView para exibir uma Lista de Itens na Barra de Pesquisa da HomePage
# Obs.: passando o parâmetro LoginRequiredMixin para que o usuário tenha que fazer obrigatóriamente o login para acessar a página
class Pesquisa_filme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    # Definindo o Modelo do Banco de Dados, o Contexto, puxa a Lista de Filmes e passa para o arquivo HTML como sendo uma object_list (passar para o homefilmes.html em substituição a lista_filmes)
    model = Filme
    # object_list -> lista de itens do modelo
    
    # Usando o get_queryset() para pegar os parâmetros (tudo o que vem após a ? na Barra do Navegador) da Busca, passando essa edição de Busca para o object_list e fazendo um filtro para obter somente os filmes que contenham a String digitada na Barra de Pesquisa da HomePage
    def get_queryset(self):
        # Capturando a informação da Barra do Navegador na HomePage
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains = termo_pesquisa)
            return object_list
        else:
            return None
        
        

# Definindo a classe Paginaperfil, usando um Novo Estilo de View: o UpdateView
# Obs.1: o UpdateView reconhece o modelo, ou seja, as tabelas do banco de dados que serão utilizadas e automaticamente carrega dentro do Html um formulário com os campos que forem definidos para serem atualizados, por exemplo model = Usuario e fields = ['first_name', 'last_name', 'email']
# Obs.2: passando o parâmetro LoginRequiredMixin para que o usuário tenha que fazer obrigatóriamente o login para acessar a página
class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']
    
    # Definindo a função obrigatória sempre que for criada uma UpdateView, para o caso de o Formulário ser bem sucedido
    def get_success_url(self):
        # Usando o reverse() para retornar um texto de Link como resposta, para onde o usuário será direcionado
        # Obs.1: importar a biblioreta reverse
        # Obs.2: não pode ser um redirect('filme:homefilmes') pois não é um Link, precisa ser um texto de Link que corresponde ao Link do 'filme:homefilmes'
        return reverse('filme:homefilmes')


# Definindo a classe Criarconta
# Obs.: Criando um usuário no Banco de Dados
class Criarconta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm
    
    # Definindo a função que verifica se o Formulário é válido (se todos os campos foram preenchidos corretamente)
    def form_valid(self, form):
        # Salvando o Formulário para que o Usuário seja criado no Banco de Dados
        form.save()
        # Retornoando o resultado
        return super().form_valid(form)
    
   
    # Definindo a função obrigatória sempre que for criada uma FormView, para o caso de o Formulário ser bem sucedido
    def get_success_url(self):
        # Usando o reverse() para retornar um texto de Link como resposta, para onde o usuário será direcionado
        # Obs.1: importar a biblioreta reverse
        # Obs.2: não pode ser um redirect('filme:login') pois não é um Link, precisa ser um texto de Link que corresponde ao Link do 'filme:login'
        return reverse('filme:login')
        



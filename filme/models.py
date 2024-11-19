# NO MODELS SÃO CRIADAS AS TABELAS DO BANCO DE DADOS

# Ver a Documentação para o django-admin and manage.py: https://docs.djangoproject.com/en/5.1/ref/django-admin/

# Criando um Novo Projeto
# django-admin startproject hashflix .

# Executando o Projeto e abrindo o link criado no Navegador: http://127.0.0.1:8000
# python manage.py runserver

# Criar o Super Usuário, definir login e senha para acessar em http://127.0.0.1:8000/admin/
# python manage.py createsuperuser

# Criando um APP do site
# django-admin startapp filme

# Sempre que for construir um site, para cada página será necessário construir 3 coisas: 
# url
# view
# template

# Obs.1: Sempre que o arquivo models.py for editado (criando uma nova tabela ou estrutura) deverão ser rodados no Terminal: 
# python manage.py makemigrations
# python manage.py makemigrate

# Obs.2: Registrar o APP criado no admin.py para que ele seja exibido no Administrativo do site

# Obs.3: Sempre que criar um Novo APP:
# 1º) fazer as configurações em settings.py (quem diz como as coisas no Django estão se conectando), para a instalação do APP
# 2º) fazer as configurações de urls.py para garantir que os links do APP aparecerão dentro do administrativo
# 3º) fazer as configurações de models.py criando a estrutura e as tabelas para garantir que elas aparecerão dentro do administrativo e sejam criadas no Banco de Dados





# Importando biblioteca(s)
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.


# CRIAR A ESTRUTURA / TABELAS DO FILME

# Criando uma constante para as Categorias
# Obs.: como sendo uma Tupla de Tuplas
LISTA_CATEGORIAS = (
    # (como será armazenada no bd, como será exibida para o usuário)
    ("ANALISES", "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)

# Criando a classe filme e passando obrigatóriamente um subclasse da classe Model
class Filme(models.Model):
    # Criando os campos da tabela
    # Obs.: definindo quais tipos e tamanhos eles receberão
    titulo = models.CharField(max_length=100) 
    descricao = models.TextField(max_length=1000)
    # Usando o ImageField() e passando no parâmetro upload_to o local onde será gravada a imagem
    # Obs.: 
    thumb = models.ImageField(upload_to="thumb_filmes")
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    # Usando timezone.now (sem parentesis) para registrar automaticamente a data e hora que o filme foi criado
    data_criacao = models.DateTimeField(default=timezone.now)
    
    
    # Usando uma Função Padrão que diz para cada Classe do Python o que aparecerá quando o usuário der um Print em algum item dessa Classe
    # Obs.1: o __str__ diz qual é o formato de String para um Objeto dessa Classe
    # Obs.2: o parâmetro self refere-se a uma Instância da Classe Filme
    def __str__(self):
        return self.titulo
    
    


# CRIAR A ESTRUTURA / TABELAS DOS EPISÓDIOS
class Episodio(models.Model):
    # Este episódio faz parte de qual filme? Como se fosse uma Chave Estrangeira.
    # Obs.1: este campo de Chave Estrangeira deverá ser o primeiro campo a ser definido
    # Obs.2: cria uma relação com o item filme de outra tabela. Esta relação é de um para muitos, sendo que um filme pode ter vários episódios mas um episódio só poderá ter um filme relacionado a ele
    # Obs.3: passar como parâmetros:
    # 1) uma String (entre aspas) contendo o nome da Tabela com que ele vai se relacionar;
    # 2) related_name="episodios" que poderá ser utilizado em algum local do código para saber quais são os episódios de um determinado filme;
    # 3) on_delete=models.CASCADE para que sejam deletados os episódios relacionados no caso de o filme ser deletado
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    # Alternativamente temos a opção models.ManyToManyField() que faz a relação de muitos filmes para muitos episódios e vice-versa, mas não é esse o caso para o projeto que estamos desenvolvendo
    # filme = models.ManyToManyField()
    
    # Criando os campos da tabela
    # Obs.: definindo quais tipos e tamanhos eles receberão
    titulo = models.CharField(max_length=100) 
    # Definindo o link do vídeo como um URLField
    video = models.URLField()
    
    # Usando uma Função Padrão que diz para cada Classe do Python o que aparecerá quando o usuário der um Print em algum item dessa Classe
    # Obs.1: o __str__ diz qual é o formato de String para um Objeto dessa Classe
    # Obs.2: o parâmetro self refere-se a uma Instância da Classe Filme
    def __str__(self):
        return self.filme.titulo + " - " + self.titulo

    


# CRIAR A ESTRUTURA / TABELAS DOS USUÁRIOS
class Usuario(AbstractUser):
    # relação de muitos para muitos
    filmes_vistos = models.ManyToManyField("Filme")






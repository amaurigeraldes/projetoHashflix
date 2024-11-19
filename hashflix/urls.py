"""
URL configuration for hashflix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# Criando os Padrões dos Links do Site
# Obs.: incluindo o path para o App filme e importando a biblioteca include
urlpatterns = [
    path('admin/', admin.site.urls),
    # Fazendo o link com o APP filme
    # Obs.1: deixando vazio, '' para gerenciar todos os links do site
    # Obs.2: passando o parâmetro namespace = "filme" que associa o arquivo de URL´s do App filme definido em app_name = "filme" ao arquivo de URL´s Padrão
    path('', include('filme.urls', namespace = "filme")),
] 

# Adicionando ao urlpatterns o link que possa carregar nas suas páginas onde as imagens serão armazenadas os 
# Obs.: obter o código abaixo e importar as bibliotecas conforme documentação 
# https://docs.djangoproject.com/en/5.1/howto/static-files/
# Serving static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Serving files uploaded by a user during developmen
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
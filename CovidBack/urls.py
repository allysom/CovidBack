"""CovidBack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from exame import views as exame_view



urlpatterns = [
    path('', exame_view.login, name='login'),
    path('login', exame_view.login, name='login'),
    path('cadastro', exame_view.cadastro, name='cadastro'),
    path('perfil', exame_view.perfil, name='perfil'),
    path('admin/', admin.site.urls),
    # ex: /exame/
    path('menu', exame_view.menu, name='menu'),
    path('exame/', exame_view.index, name='exame'),
    path('exame/add', exame_view.exame_add, name='exame-add'),
    # ex: /exame/5/
    path('exame/<int:exame_id>', exame_view.detail, name='detail'),
    path('logout', exame_view.logout, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

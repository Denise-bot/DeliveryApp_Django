from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.home, name='home'),
    path("categoria/<int:id>", views.categorias, name='categoria'),
    path("produto/<int:id>", views.produto, name='produto'),
    path("add_carrinho", views.add_carrinho, name='add_carrinho'),
    path("ver_carrinho", views.ver_carrinho, name='ver_carrinho'),
    path("remover_carrinho/<int:id>", views.remover_carrinho, name='remover_carrinho'),
    path("login/", views.login_view, name='login'),
    path("cadastro/", views.cadastro_view, name='cadastro'),
    path("logout/", LogoutView.as_view(next_page='home'), name='logout'),
    path("perfil/", views.perfil_view, name='perfil'),
]

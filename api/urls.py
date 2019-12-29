from django.urls import path
from usermanager.views import UserList
from products.views import ProductList
from products.views import CategoryList

urlpatterns  = [
    path('usuarios/',UserList.as_view(), name = 'usuarios_list'),
    path('categorias/',CategoryList.as_view(), name = 'categorias_list'),
    path('productos/',ProductList.as_view(), name = 'productos_list'),
]
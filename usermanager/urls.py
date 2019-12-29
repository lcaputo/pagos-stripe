from django.urls import path
from usermanager.views import UserList

urlpatterns  = [
    path('usuarios/',UserList.as_view(), name = 'usuarios_list'),
]
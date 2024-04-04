from django.urls import path

from usuarios.views import CustomLoginView, LogoutView, UsuarioCreateView

app_name = 'usuarios'

urlpatterns = [
    path('registrar/', UsuarioCreateView.as_view(), name='registrar-usuario'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),
]

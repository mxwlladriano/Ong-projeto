from django.urls import path
from cadastro.views import AutocompleteCadastroView, BeneficioCreateView, CadastroCreateView, CadastroListView, CadastroDetailView

app_name = 'cadastro'

urlpatterns = [
    path('', CadastroCreateView.as_view(), name='cadastrar'),
    path('listar-cadastros/', CadastroListView.as_view(), name='listar-cadastros'),
    path('ver-detalhes/<int:pk>/', CadastroDetailView.as_view(), name='ver-detalhes'),
    path('add-beneficio/', BeneficioCreateView.as_view(), name='add-beneficio'),
    path('autocomplete-cadastro/', AutocompleteCadastroView.as_view(), name='autocomplete_cadastro'),

]

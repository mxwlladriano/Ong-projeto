from django.views.generic import ListView
from cadastro.models import Cadastro
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from cadastro.models import Beneficio
from cadastro.models.Beneficio import BENEFICIOS_CHOICES
from cadastro.models.CaracterizacaoMausTratos import TIPO_VIOLENCIA_CHOICES
from usuarios.forms import UsuarioCreateForm

class CadastroListView(LoginRequiredMixin, ListView):
    template_name = 'listar-cadastros.html' 
    model = Cadastro
    paginate_by = 7

    def get_queryset(self):
        searchQuery = self.request.GET.get('search', '')
        userUnidade = self.request.user.unidade

        queryset = Cadastro.objects.all().order_by('nome')

        # Aplicar filtro de pesquisa
        if searchQuery:
            queryset = queryset.filter(
                Q(nome__icontains=searchQuery) | Q(cpf__icontains=searchQuery)
            )

        # Aplicar outros filtros
        idade = self.request.GET.get('idade')
        sexo = self.request.GET.get('sexo')
        tipoViolencia = self.request.GET.get('tipoViolencia')
        beneficio = self.request.GET.get('beneficio')
        dataEntrada = self.request.GET.get('dataEntrada')
        dataSaida = self.request.GET.get('dataSaida')
        causaAcolhimento = self.request.GET.get('causaAcolhimento')
        if idade:
            queryset = queryset.filter(idade=idade)
        if sexo:
            queryset = queryset.filter(sexo=sexo)
        if tipoViolencia:
            queryset = queryset.filter(caracterizacaoMausTratos__tipoViolencia=tipoViolencia)
        if beneficio:
            cadastrosIds = Beneficio.objects.filter(nome=beneficio).values_list('beneficiado_id', flat=True)
            queryset = queryset.filter(id__in=cadastrosIds)
        if dataEntrada:
            queryset = queryset.filter(acolhimento__dataEntrada=dataEntrada)
        if dataSaida:
            queryset = queryset.filter(acolhimento__dataSaida=dataSaida)
        if causaAcolhimento:
            queryset = queryset.filter(acolhimento__causaAcolhimento=causaAcolhimento)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["usuario"] = UsuarioCreateForm()
        context["beneficios"] = BENEFICIOS_CHOICES
        context["tiposViolencias"] = TIPO_VIOLENCIA_CHOICES

        return context
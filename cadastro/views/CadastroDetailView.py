from django.views.generic import DetailView
from cadastro.models import Beneficio
from cadastro.models.Cadastro import Cadastro

class CadastroDetailView(DetailView):
    model = Cadastro
    template_name = 'ver-detalhes-cadastro.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cadastro = self.get_object()

        context['composicaoFamiliar'] = cadastro.composicaoFamiliar.all()
        context['beneficios'] = Beneficio.objects.filter(beneficiado=cadastro)
        
        return context
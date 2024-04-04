from django.views.generic.edit import CreateView
from django.contrib import messages
from django.urls import reverse
from cadastro.models import Beneficio
from cadastro.forms import BeneficioForm
from usuarios.forms import UsuarioCreateForm

class BeneficioCreateView(CreateView):
    model = Beneficio
    form_class = BeneficioForm
    template_name = 'add-beneficios.html'  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["usuario"] = UsuarioCreateForm()
        return context
    
    def form_valid(self, form):
        print("Dados do formulário:", form.cleaned_data) 
        form.instance.qmCadastrou = self.request.user
        return super().form_valid(form)
        
    def form_invalid(self, form):
        print("Formulário inválido:", form.errors)  # Adiciona um print dos erros de validação do formulário
        return super().form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, 'Benefício adicionado com sucesso!')
        return reverse('cadastro:cadastrar')

from django.views.generic.edit import CreateView
from cadastro.forms import AcolhimentoForm, CaracterizacaoMausTratosForm, ComposicaoFamiliarForm, DadosResponsavelForm, DenuncianteCondutaForm, OrigemDemandaForm, SituacaoHabitacionalForm

from cadastro.forms.CadastroForm import CadastroForm
from cadastro.models import Cadastro
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from usuarios.forms import UsuarioCreateForm

class CadastroCreateView(LoginRequiredMixin, CreateView):
    template_name = 'index.html' 
    model = Cadastro
    form_class = CadastroForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["usuario"] = UsuarioCreateForm()

        context["origemDemanda"] = OrigemDemandaForm()
        context["caracterizacaoMausTratos"] = CaracterizacaoMausTratosForm()
        context["denuncianteConduta"] = DenuncianteCondutaForm()
        context["situacaoHabitacional"] = SituacaoHabitacionalForm()
        context["dadosResponsavel"] = DadosResponsavelForm()
        context["composicaoFamiliar"] = ComposicaoFamiliarForm()
        context["acolhimento"] = AcolhimentoForm()

        return context

    def form_valid(self, form):
        
        form.instance.qmCadastrou = self.request.user
        faixaEtaria = form.cleaned_data.get('faixaEtaria')
        numSequencial = Cadastro.objects.filter(faixaEtaria=faixaEtaria).count() + 1
        numProntuario = f"{numSequencial}"
        form.instance.numeroProntuario = numProntuario
        
        acolhimentoForm = AcolhimentoForm(self.request.POST)
        origemDemandaForm = OrigemDemandaForm(self.request.POST)
        cMausTratosForm = CaracterizacaoMausTratosForm(self.request.POST)
        dCondutaForm = DenuncianteCondutaForm(self.request.POST)
        sitHabitacionalForm = SituacaoHabitacionalForm(self.request.POST)
        dadosResponsavelForm = DadosResponsavelForm(self.request.POST)
        compFamiliarForm = ComposicaoFamiliarForm(self.request.POST)

        self.object = form.save()  # Salva o formulário principal

        try:
            acolhimento = acolhimentoForm.save()
            self.object.acolhimento = acolhimento  # Atribui o acolhimento ao cadastro
            self.object.save()
        except:
            self.object.acolhimento = None
            self.object.save()

        try:
            origemDemanda = origemDemandaForm.save()
            self.object.origemDemanda = origemDemanda  # Atribui a origem da demanda ao cadastro
            self.object.save()
        except:
            self.object.origemDemanda = None
            self.object.save()
        
        try:
            cMausTratos = cMausTratosForm.save()
            self.object.caracterizacaoMausTratos = cMausTratos  # Atribui a caracterização de maus-tratos ao cadastro
            self.object.save()
        except:
            self.object.caracterizacaoMausTratos = None
            self.object.save()
        
        try:
            dConduta = dCondutaForm.save()
            self.object.denuncianteConduta = dConduta  # Atribui a denúncia de conduta ao cadastro
            self.object.save()
        except:
            self.object.denuncianteConduta = None
            self.object.save()

        try:
            sitHabitacional = sitHabitacionalForm.save()
            self.object.situacaoHabitacional = sitHabitacional  # Atribui a situação habitacional ao cadastro
            self.object.save()
        except:
            self.object.situacaoHabitacional = None
            self.object.save()

        try:
            dadosResponsavel = dadosResponsavelForm.save()
            self.object.dadosResponsavel = dadosResponsavel  # Atribui os dados do responsável ao cadastro
            self.object.save()
        except:
            self.object.dadosResponsavel = None
            self.object.save()

        try:
            compFamiliar = compFamiliarForm.save()
            self.object.composicaoFamiliar.set([compFamiliar])  # Atribui a composição familiar ao cadastro
            self.object.save()
        except:
            self.object.composicaoFamiliar.set([None])
            self.object.save()
        
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_success_url(self):
        messages.success(self.request, 'Cadastro adicionado com sucesso!')
        return reverse('cadastro:cadastrar')

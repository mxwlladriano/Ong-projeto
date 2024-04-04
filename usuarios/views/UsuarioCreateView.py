from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from usuarios.forms import UsuarioCreateForm

class UsuarioCreateView(CreateView):
    template_name = 'base.html'
    form_class = UsuarioCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.get_form)
        context['usuario'] = self.get_form()
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        if not form.cleaned_data['unidade']:
            user.is_superuser = True  
        user.save()
        return redirect('cadastro:cadastrar')
    
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
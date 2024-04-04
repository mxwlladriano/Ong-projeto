from django.http import JsonResponse
from django.views import View
from cadastro.models import Cadastro

class AutocompleteCadastroView(View):
    def get(self, request, *args, **kwargs):
        term = request.GET.get('term')

        if term:
            cadastros = Cadastro.objects.filter(nome__icontains=term)
            results = [{'id': cadastro.id, 'nome': cadastro.nome, 'cpf': cadastro.cpf} for cadastro in cadastros]
        else:
            results = []

        return JsonResponse(results, safe=False)
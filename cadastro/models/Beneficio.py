from django.db import models

from cadastro.models import Cadastro
from usuarios.models import Usuario

BENEFICIOS_CHOICES = [
    ('cesta_basica', 'Cesta Básica'),
    ('auxilio_funeario', 'Auxílio Funerário'),
    ('aluguel_social', 'Aluguel Social'),
    ('auxilio_enxoval', 'Auxílio Enxoval'),
    ('auxilio_passagem', 'Auxílio Passagem'),
    ('ajuda_custo_temporaria', 'Ajuda de Custo Temporária')
]

class Beneficio(models.Model):
    nome = models.CharField(max_length=100, choices=BENEFICIOS_CHOICES)
    beneficiado = models.ForeignKey(Cadastro, on_delete=models.CASCADE)
    qmCadastrou = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    dataCadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True)

from django.db import models

CONDUCAO_CHOICES = [
    ('conselho_tutelar', 'Conselho Tutelar'),
    ('poder_judiciario', 'Poder Judiciário'),
    ('outro', 'Outro'),
]
DOCUMENTOS_CHOICES = [
    ('declaracao_nascido_vivo', 'Declaração de Nascido Vivo'),
    ('certidao_nascimento', 'Certidão de Nascimento'),
    ('carteira_vacinacao', 'Carteira de Vacinação'),
    ('cartao_sus', 'Cartão do SUS'),
    ('carteira_identidade', 'Carteira de Identidade'),
    ('cpf', 'CPF'),
    ('titulo_eleitor', 'Título de Eleitor'),
    ('matricula_escolar', 'Matrícula Escolar'),
    ('materiais_escolares', 'Materiais Escolares'),
    ('outros', 'Outros'),
]

class Acolhimento(models.Model):
    dataEntrada = models.DateField(verbose_name='Data de Entrada', null=True, blank=True)
    dataSaida = models.DateField(verbose_name='Data de Saída', null=True, blank=True)
    causaAcolhimento = models.TextField(verbose_name='Causa do Acolhimento', null=True, blank=True)
    acompanhamentoAudiencia = models.TextField(verbose_name='Está em Acompanhamento de Audiência', null=True, blank=True)
    guiaDeAcolhimento = models.BooleanField(blank=True, null=True, verbose_name='Tem guia de Acolhimento?')
    conduzidaAoAcolhimento = models.CharField(max_length=255, verbose_name='Conduzida ao Acolhimento por', choices=CONDUCAO_CHOICES, blank=True, null=True)
    conduzidaAoAcolhimentoOutros = models.TextField(verbose_name='Descrição (se escolhido "Outros")', blank=True, null=True)
    documentosRecebidos = models.CharField(max_length=255, verbose_name='Documentos do acolhido recebidos', choices=DOCUMENTOS_CHOICES, blank=True, null=True)
    documentosRecebidosOutros = models.TextField(verbose_name='Descrição (se escolhido "Outros")', blank=True, null=True)
    objetosPessoaisRecebidos = models.TextField(verbose_name='Objetos pessoais recebidos', blank=True, null=True)
    condicoesFisicas = models.TextField(verbose_name='Condições físicas', blank=True, null=True)
    profissionalQueRecebeu = models.CharField(max_length=255, verbose_name='Profissional que recebeu', blank=True, null=True)

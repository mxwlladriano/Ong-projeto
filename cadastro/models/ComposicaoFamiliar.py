from django.db import models

ESCOLARIDADE_CHOICES = [
    ('fundamental', 'Fundamental'),
    ('medio', 'Médio'),
    ('superior', 'Superior'),
]

class ComposicaoFamiliar(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome do Familiar', blank=True, null=True)
    idade = models.IntegerField(verbose_name='Idade do Familiar', blank=True, null=True)
    parentesco = models.CharField(max_length=255, verbose_name='Parentesco com o Responsável', blank=True, null=True)
    escolaridade = models.CharField(max_length=255, verbose_name='Escolaridade do Familiar', choices=ESCOLARIDADE_CHOICES, blank=True, null=True)
    ocupacao = models.CharField(max_length=255, verbose_name='Ocupação do Familiar', blank=True, null=True)
    renda = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Renda do Familiar', blank=True, null=True)

    def __str__(self):
        return self.nome

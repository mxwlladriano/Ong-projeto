from django.db import models

SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

class DadosResponsavel(models.Model):
    nome = models.CharField(null=True, blank=True, max_length=255, verbose_name='Nome do Responsável')
    idade = models.IntegerField(null=True, blank=True, verbose_name='Idade do Responsável')
    dataNascimento = models.DateField(blank=True, null=True, verbose_name='Data de Nascimento do Responsável')
    sexo = models.CharField(null=True, blank=True, max_length=255, choices=SEXO_CHOICES, verbose_name='Sexo do Responsável')
    cor = models.CharField(null=True, blank=True, max_length=255, verbose_name='Cor do Responsável')
    enderecoResponsavel = models.CharField(null=True, blank=True, max_length=255, verbose_name='Endereco do Responsável')
    telefone = models.CharField(null=True, blank=True, max_length=255, verbose_name='Telefone do Responsável')
    
    def __str__(self):
        return self.nome

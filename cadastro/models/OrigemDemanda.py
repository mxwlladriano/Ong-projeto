from django.db import models
from multiselectfield import MultiSelectField

POLITICAS_PUBLICAS_CHOICES = [
    ('procura_espontanea', 'Procura Espontânea'),
    ('creas', 'Creas'),
    ('conselho_tutelar', 'Conselho Tutelar'),
    # ... outras opções ...
    ('outros_politicas_publicas', 'Outros Políticas Públicas'),
]

INDICACAO_OUTROS_CHOICES = [
    ('outros_indique', 'Outros, indique'),
]

ENCAMINHAMENTO_CHOICES = [
    ('relatorio_informativo', 'Relatório informativo'),
    ('paf', 'PAF'),
    # ... outras opções ...
    ('outro_encaminhamento', 'Outro Encaminhamento'),
]

PERFIL_TITULAR_CHOICES = [
    ('crianca_adolescente', 'Criança e Adolescente'),
    ('homem', 'Homem'),
    # ... outras opções ...
    ('outro_perfil_titular', 'Outro Perfil Titular'),
]


ESTUDA_CHOICES = [
    ('estuda', 'Estuda'),
]

TRABALHA_CHOICES = [
    ('trabalha', 'Trabalha'),
]

PROGRAMAS_SOCIAIS_CHOICES = [
    ('insercao_programas_sociais', 'Inserção em programas sociais'),
    ('pbf', 'PBF'),
    # ... outras opções ...
    ('outro_programa_social', 'Outro Programa Social'),
]

DEFICIENCIA_CHOICES = [
    ('apresenta_deficiencia_fisica', 'Apresenta deficiência física'),
    ('fisica', 'Física'),
    # ... outras opções ...
    ('outro_deficiencia', 'Outra Deficiência'),
]

class OrigemDemanda(models.Model):
    origemDemandaPoliticasPublicas = MultiSelectField(
        max_length=255, choices=POLITICAS_PUBLICAS_CHOICES,
        blank=True,
        null=True,
        verbose_name='Origem de Demanda - Políticas Públicas'
    )    
    origemDemandaPoliticasPublicasOutros = models.CharField(max_length=255, blank=True, null=True, verbose_name='Outros Políticas Públicas')

    origemDemandaOutrosIndique = MultiSelectField(
        max_length=255, choices=INDICACAO_OUTROS_CHOICES,
        blank=True,
        null=True,
        verbose_name='Origem de Demanda - Outros, indique'
    )    
    origemDemandaOutrosIndiqueOutros = models.CharField(max_length=255, blank=True, null=True, verbose_name='Outro Texto Outros, Indique')

    origemDemandaEncaminhamento = MultiSelectField(
        max_length=255, choices=ENCAMINHAMENTO_CHOICES,
        blank=True,
        null=True,
        verbose_name='Origem de Demanda - Encaminhamento'
    )    
    origemDemandaEncaminhamentoOutro = models.CharField(max_length=255, blank=True, null=True, verbose_name='Outro Encaminhamento')

    origemDemandaPerfilTitular = MultiSelectField(
        max_length=255, choices=PERFIL_TITULAR_CHOICES,
        blank=True,
        null=True,
        verbose_name='Origem de Demanda - Perfil Titular'
    )    
    origemDemandaPerfilTitularOutro = models.CharField(max_length=255, blank=True, null=True, verbose_name='Outro Perfil Titular')


    origemDemandaEstuda = MultiSelectField(
        max_length=255, choices=ESTUDA_CHOICES,
        blank=True,
        null=True,
        verbose_name='Origem de Demanda - Estuda'
    )    
    
    origemDemandaTrabalha = MultiSelectField(
        max_length=255, choices=TRABALHA_CHOICES,
        blank=True,
        null=True,
        verbose_name='Origem de Demanda - Trabalha'
    )


    origemDemandaProgramasSociais = MultiSelectField(
        max_length=255, choices=PROGRAMAS_SOCIAIS_CHOICES,
        verbose_name='Origem de Demanda - Programas Sociais'
    )

    origemDemandaProgramasSociaisOutro = models.CharField(max_length=255, blank=True, null=True, verbose_name='Outro Programa Social')

    origemDemandaDeficiencia = MultiSelectField(
        max_length=255, choices=DEFICIENCIA_CHOICES,
        blank=True,
        null=True,
        verbose_name='Origem de Demanda - Deficiência'
    )

    origemDemandaDeficienciaOutro = models.CharField(max_length=255, blank=True, null=True, verbose_name='Outra Deficiência')



    def __str__(self):
        return "Origem de Demanda {}".format(self.id)

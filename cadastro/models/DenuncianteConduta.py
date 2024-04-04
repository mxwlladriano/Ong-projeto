from django.db import models
from multiselectfield import MultiSelectField

GRAU_RELACIONAMENTO_CHOICES = [
    ('denunciante_propria_vitima', 'Própria vítima'),
    ('denunciante_outros', 'Outros'),
    ('denunciante_nao_cabe', 'Não cabe(s'),
]
CONDUTA_ENCAMINHAMENTO_CHOICES = [
    ('conduta_encaminhamento', 'Encaminhamento'),
    ('conduta_outros', 'Outros'),
]
ASSISTENCIA_CHOICES = [
    ('assistencia_hospital_regional', 'Hospital Regional'),
    ('assistencia_nasf', 'NASF'),
    ('assistencia_tfd', 'TFD'),
]
RESIDE_CHOICES = [
    ('reside_pai', 'Pai'),
    ('reside_mae', 'Mãe'),
    ('reside_padastro', 'Padastro'),
    ('reside_madastra', 'Madastra'),
    ('reside_tios', 'Tios'),
    ('reside_avos', 'Avós'),
    ('reside_irmaos', 'Irmãos'),
    ('reside_filhos', 'Filhos'),
    ('reside_mora_sozinho', 'Mora só'),
    ('reside_conjuge', 'Cônjuge'),
    ('reside_outro', 'Outro'),
]


class DenuncianteConduta(models.Model):
    denuncianteGrauRelacionamento = models.CharField(max_length=255, choices=GRAU_RELACIONAMENTO_CHOICES,
        blank=True,
        null=True,
        verbose_name='Grau de Relacionamento'
    )    
    denuncianteGrauRelacionamentoOutro = models.CharField(max_length=255, blank=True, null=True, verbose_name='Outro - Grau de Relacionamento')

    condutaEspecificar = models.CharField(max_length=255, choices=CONDUTA_ENCAMINHAMENTO_CHOICES,
        blank=True,
        null=True,
        verbose_name='Especificar'
    )

    condutaEspecificarOutro = models.CharField(max_length=255, blank=True, null=True, verbose_name='Outro - Especificar')
    condutaSinaisViolencia = models.CharField(max_length=255, blank=True, null=True, verbose_name='Sinais de Violência')

    assistenciaPostoSaude = models.CharField(max_length=255, choices=ASSISTENCIA_CHOICES,
        blank=True,
        null=True,
        verbose_name='Posto de Saúde'
    )

    assistenciaAgenteSaude = models.CharField(max_length=255, blank=True, null=True, verbose_name='Agente de Saúde')

    resideCom = MultiSelectField(max_length=255, choices=RESIDE_CHOICES,
        blank=True,
        null=True,
        verbose_name='Reside com ?'
    )

    resideOutro = models.CharField(max_length=255, blank=True, null=True, verbose_name='Outro - Especificar')

    def __str__(self):
        return self.denuncianteGrauRelacionamento if self.denuncianteGrauRelacionamento else ''


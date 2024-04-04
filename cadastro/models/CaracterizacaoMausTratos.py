from django.db import models
from multiselectfield import MultiSelectField

AGRESSOR_CHOICES = [
    ('suposto_agressor_pai', 'Pai'),
    ('suposto_agressor_mae', 'Mãe'),
    ('suposto_agressor_filho', 'Filho(s'),
    ('suposto_agressor_padastro', 'Padastro'),
    ('suposto_agressor_madastra', 'Madastra'),
    ('suposto_agressor_vizinho', 'Vizinho'),
    ('suposto_agressor_conjuge', 'Cônjuge'),
    ('suposto_agressor_outros', 'Outros'),
]
TIPO_VIOLENCIA_CHOICES = [
    ('tipo_violencia_intrafamiliar', 'Intrafamiliar'),
    ('tipo_violencia_extrafamiliar', 'Extrafamiliar'),
    ('tipo_violencia_negligencia', 'Negligência'),
    ('tipo_violencia_fisica', 'Física'),
    ('tipo_violencia_psicologica_moral', 'Psicológica/Moral'),
    ('tipo_violencia_tortura', 'Tortura'),
    ('tipo_violencia_trafico_humanos', 'Tráfico de Humanos'),
    ('tipo_violencia_financeira_economica', 'Financeira/Econômica'),
    ('tipo_violencia_trabalho_infantil', 'Trabalho Infantil'),
    ('tipo_violencia_discriminacao_genero', 'Discriminação de Gênero'),
    ('tipo_violencia_sexual_descricao', 'Violência Sexual (Descrição)'),
    ('tipo_violencia_outros', 'Outros'),
]
CARACTERISTICA_AGRESSAO_CHOICES = [
    ('caracteristica_agressao_uma_vez', 'Uma vez'),
    ('caracteristica_agressao_mais_de_uma_vez', 'Mais de uma vez'),
]
CARACTERISTICA_AGRESSAO_PERIODO_CHOICES = [
    ('caracteristica_agressao_manha', 'Manhã'),
    ('caracteristica_agressao_tarde', 'Tarde'),
    ('caracteristica_agressao_noite', 'Noite'),
]
LOCAL_OCORRENCIA_CHOICES = [
    ('local_ocorrencia_residencia', 'Residência'),
    ('local_ocorrencia_habitacao_coletiva', 'Habitação Coletiva'),
    ('local_ocorrencia_escola', 'Escola'),
    ('local_ocorrencia_espaco_pratica_esportiva', 'Espaço de Prática Esportiva'),
    ('local_ocorrencia_bar_ou_similar', 'Bar ou Similar'),
    ('local_ocorrencia_via_publica', 'Via Pública'),
    ('local_ocorrencia_comercio_servicos', 'Comércio/Serviços'),
    ('local_ocorrencia_industria_construcao', 'Indústria/Construção'),
    ('local_ocorrencia_outro', 'Outro'),
]

class CaracterizacaoMausTratos(models.Model):
    supostoAgressor = MultiSelectField(
        max_length=255, choices=AGRESSOR_CHOICES,
        blank=True,
        null=True,
        verbose_name='Suposto Agressor'
    )   
     
    supostoAgressorOutrosDescricao = models.CharField(max_length=255, blank=True, null=True, verbose_name='Outros (Suposto Agressor)')
    
    tipoViolencia = MultiSelectField(
        max_length=255, choices=TIPO_VIOLENCIA_CHOICES,
        blank=True,
        null=True,
        verbose_name='Tipo de Violência'
    )    
    tipoViolenciaOutrosDescricao = models.CharField(max_length=255, blank=True, null=True, verbose_name='Outros (Tipo de Violência)')
    tipoViolenciaSexualDescricao = models.CharField(max_length=255, blank=True, null=True, verbose_name='Violência Sexual (Descrição)')
    
    caracteristicaAgressao = MultiSelectField(
        max_length=255, choices=CARACTERISTICA_AGRESSAO_CHOICES,
        blank=True,
        null=True,
        verbose_name='Característica da Agressão'
    )
    caracteristicaAgressaoDataPeriodo = models.DateField(null=True, blank=True, verbose_name='Data ou Período da Agressão')
    caracteristicaAgressaoPeriodo = MultiSelectField(
        max_length=255, choices=CARACTERISTICA_AGRESSAO_PERIODO_CHOICES,
        blank=True,
        null=True,
        verbose_name='Período da Agressão'
    )    
    localOcorrencia = MultiSelectField(
        max_length=255, choices=LOCAL_OCORRENCIA_CHOICES,
        blank=True,
        null=True,
        verbose_name='Local da Ocorrência'
    )    
    localOcorrenciaOutroDescricao = models.CharField(max_length=255, blank=True, null=True, verbose_name='Outro (Local da Ocorrência)')    
    enderecoLocalOcorrencia = models.CharField(max_length=255, blank=True, null=True, verbose_name='Endereço Local Ocorrência')
    
    def __str__(self):
        return "Caracterização de Maus Tratos {}".format(self.id)

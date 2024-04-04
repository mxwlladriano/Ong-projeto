from django.db import models

MORADIA_CHOICES = [
    ('moradia_casa', 'Casa'),
    ('moradia_apto', 'Apto'),
    ('moradia_kitnet', 'Kitnet'),
]
CARACTERISTICAS_CHOICES = [
    ('caracteristicas_propria', 'Própria'),
    ('caracteristicas_alugada', 'Alugada'),
    ('caracteristicas_alvenaria', 'Alvenaria'),
    ('caracteristicas_cedida', 'Cedida'),
    ('caracteristicas_palha', 'Palha'),
    ('caracteristicas_taipa_outros', 'Taipa/Outros'),
]
TERRITORIO_CHOICES = [
    ('territorio_acessibilidade_interno', 'Acessibilidade para pessoas com dificuldade de locomoção - Interno'),
    ('territorio_acessibilidade_externo', 'Acessibilidade para pessoas com dificuldade de locomoção - Externo'),
    ('territorio_acessibilidade_nenhum', 'Acessibilidade para pessoas com dificuldade de locomoção - Nenhum'),
    ('territorio_local_dificil_acesso_geo', 'Local com difícil acesso geo'),
    ('territorio_risco_desabamento_alagamento', 'Risco de desabamento e alagamento'),
    ('territorio_forte_presenca_viol', 'Forte presença de viol'),
]
ESTRUTURA_RUA_CHOICES = [
    ('estrutura_rua_asfalto', 'Asfalto'),
    ('estrutura_rua_picarra', 'Piçarra'),
    ('estrutura_rua_sem_calcamento', 'Sem calçamento'),
]
ILUMINACAO_PUBLICA_CHOICES = [
    ('iluminacao_publica_com_medidor_proprio', 'Pública com medidor próprio'),
    ('iluminacao_publica_com_medidor_compartilhado', 'Pública com medidor compartilhado'),
    ('iluminacao_publica_sem_medidor', 'Pública sem medidor'),
    ('iluminacao_sem_energia', 'Sem energia'),
]
ABASTECIMENTO_CHOICES = [
    ('abastecimento_rede_geral_distribuicao', 'Rede geral de distribuição'),
    ('abastecimento_poco_nascente', 'Poço ou nascente'),
    ('abastecimento_cisterna_agua_chuva', 'Cisterna ou água de chuva'),
    ('abastecimento_carro_pipa', 'Carro pipa'),
    ('abastecimento_outra_forma', 'Outra forma'),
]
CONSUMO_AGUA_CHOICES = [
    ('consumo_agua_filtrada', 'Filtrada'),
    ('consumo_agua_nao_filtrada', 'Não filtrada'),
    ('consumo_agua_coada', 'Coada'),
    ('consumo_agua_fervida', 'Fervida'),
    ('consumo_agua_comprada', 'Comprada'),
]
ESGOTO_CHOICES = [
    ('esgoto_rede_coletora', 'Rede coletora'),
    ('esgoto_fossa_septica', 'Fossa séptica'),
    ('esgoto_fossa_rudimentar', 'Fossa rudimentar'),
    ('esgoto_ceu_aberto', 'Céu aberto'),
    ('esgoto_domicilio_sem_banheiro', 'Domicílio sem banheiro'),
]
LIXO_CHOICES = [
    ('lixo_coleta_publica', 'Coleta pública'),
    ('lixo_queimado', 'Queimado'),
    ('lixo_ar_livre', 'Ar livre'),
    ('lixo_enterrado', 'Enterrado'),
]
FAMILIA_CHOICES = [
    ('familia_uso_psicoativa', 'Na família alguém faz uso de psicoativa'),
    ('familia_pessoas_deficientes', 'Na família tem pessoas deficientes'),
    ('familia_vivencia_situacao_violencia', 'Vivência em situação de violência'),
]

class SituacaoHabitacional(models.Model):
    moradia = models.CharField(max_length=255, choices=MORADIA_CHOICES,
        blank=True,
        null=True,
        verbose_name='Moradia'
    )

    caracteristicas = models.CharField(max_length=255, choices=CARACTERISTICAS_CHOICES,
        blank=True,
        null=True,
        verbose_name='Características'
    )

    territorio = models.CharField(max_length=255, choices=TERRITORIO_CHOICES,
        blank=True,
        null=True,
        verbose_name='Território'
    )

    estruturaRua = models.CharField(max_length=255, choices=ESTRUTURA_RUA_CHOICES,
        blank=True,
        null=True,
        verbose_name='Estrutura da Rua'
    )

    iluminacaoPublica = models.CharField(max_length=255, choices=ILUMINACAO_PUBLICA_CHOICES,
        blank=True,
        null=True,
        verbose_name='Iluminação Pública'
    )

    abastecimento = models.CharField(max_length=255, choices=ABASTECIMENTO_CHOICES,
        blank=True,
        null=True,
        verbose_name='Abastecimento de Água'
    )

    consumoAgua = models.CharField(max_length=255, choices=CONSUMO_AGUA_CHOICES,
        blank=True,
        null=True,
        verbose_name='Consumo de Água'
    )

    esgoto = models.CharField(max_length=255, choices=ESGOTO_CHOICES,
        blank=True,
        null=True,
        verbose_name='Esgoto'
    )

    lixo = models.CharField(max_length=255, choices=LIXO_CHOICES,
        blank=True,
        null=True,
        verbose_name='Lixo'
    )

    familia = models.CharField(max_length=255, choices=FAMILIA_CHOICES,
        blank=True,
        null=True,
        verbose_name='Família'
    )

    caracteristicasNumeroComodos = models.CharField(max_length=255, blank=True, null=True, verbose_name='Números de cômodos')
    caracteristicasNumeroDormitorios = models.CharField(max_length=255, blank=True, null=True, verbose_name='Números de dormitórios')
    caracteristicasPessoasPorDormitorios = models.CharField(max_length=255, blank=True, null=True, verbose_name='Pessoas por dormitórios')

    territorioLocalDificilAcessoGeo = models.BooleanField(default=False, blank=True, null=True, verbose_name='Local com difícil acesso geografico')
    territorioRiscoDesabamentoAlagamento = models.BooleanField(default=False, blank=True, null=True, verbose_name='Risco de desabamento e alagamento')
    territorioFortePresencaViol = models.BooleanField(default=False, blank=True, null=True, verbose_name='Forte presença de violencia')

    lixoOutro = models.CharField(max_length=255, blank=True, null=True, verbose_name='Outro - Lixo')
    
    familiaUsoPsicoativaQualSpa = models.CharField(max_length=255, blank=True, null=True, verbose_name='Familia usa Psicoativo? Qual?')
    familiaUsoPsicoativaQuem = models.CharField(max_length=255, blank=True, null=True, verbose_name='Familia usa Psicoativo? Quem?')

    familiaPessoasDeficientesQuem = models.CharField(max_length=255, blank=True, null=True, verbose_name='Familia tem deficiente? Quem?')

    familiaVivenciaSituacaoViolenciaObservacao = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observação')

    def __str__(self):
        return "Situacao Habitacional {}".format(self.id)
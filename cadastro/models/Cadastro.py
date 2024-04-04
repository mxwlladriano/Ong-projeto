from django.db import models
from cadastro.models.Acolhimento import Acolhimento
from cadastro.models.ComposicaoFamiliar import ComposicaoFamiliar
from cadastro.models.DadosResponsavel import DadosResponsavel
from cadastro.models.CaracterizacaoMausTratos import CaracterizacaoMausTratos
from cadastro.models.DenuncianteConduta import DenuncianteConduta
from cadastro.models.OrigemDemanda import OrigemDemanda
from cadastro.models.SituacaoHabitacional import SituacaoHabitacional
from usuarios.models import Usuario

SEXO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outro'),
]
FAIXA_ETARIA_CHOICES = [
    ('crianca', 'Criança'),
    ('adolescente', 'Adolescente'),
    ('adulto', 'Adulto'),
    ('idoso', 'Idoso'),
]
ESTADO_CIVIL_CHOICES = [
    ('solteiro', 'Solteiro(a)'),
    ('casado', 'Casado(a)'),
    ('divorciado', 'Divorciado(a)'),
    ('viuvo', 'Viúvo(a)'),
    ('separado', 'Separado(a)'),
    ('outro', 'Outro'),
]
ESCOLARIDADE_CHOICES = [
    ('fundamental_incompleto', 'Fundamental Incompleto'),
    ('fundamental_completo', 'Fundamental Completo'),
    ('medio_incompleto', 'Médio Incompleto'),
    ('medio_completo', 'Médio Completo'),
    ('superior_incompleto', 'Superior Incompleto'),
    ('superior_completo', 'Superior Completo'),
    ('pos_graduacao', 'Pós-graduação'),
    ('mestrado', 'Mestrado'),
    ('doutorado', 'Doutorado'),
    ('outro', 'Outro'),
]
ORIENTACAO_SEXUAL_CHOICES = [
    ('heterossexual', 'Heterossexual'),
    ('homossexual', 'Homossexual'),
    ('bissexual', 'Bissexual'),
    ('pansexual', 'Pansexual'),
    ('assexual', 'Assexual'),
    ('outro', 'Outro'),
]
HORARIO_TRABALHO_CHOICES = [
    ('meio_periodo', 'Meio Período'),
    ('integral', 'Integral'), 
    ('outro', 'Outro')
]

class Cadastro(models.Model):
    numeroProntuario = models.CharField(max_length=255, verbose_name='Número do prontuario')
    dataAtendimento = models.DateField(verbose_name='Data de Atendimento')

    nome = models.CharField(max_length=100)
    dataNascimento = models.DateField()
    idade = models.IntegerField()
    apelido = models.CharField(max_length=50)
    faixaEtaria = models.CharField(
        max_length=20,
        choices=FAIXA_ETARIA_CHOICES,
        default='adulto' 
    )
    naturalidade = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)

    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    zona = models.CharField(max_length=100)
    pontoReferencia = models.CharField(max_length=255)

    telefone = models.CharField(max_length=20)
    pai = models.CharField(max_length=100)
    mae = models.CharField(max_length=100)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)
    tituloEleitor = models.CharField(max_length=20)
    nis = models.CharField(max_length=20)
    carteiraTrabalho = models.CharField(max_length=20)
    reservista = models.CharField(max_length=20)

    sexo = models.CharField(max_length=45, choices=SEXO_CHOICES, null=True, blank=True)
    orientacaoSexual = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    estadoCivil = models.CharField(max_length=50)
    escolaridade = models.CharField(max_length=100, choices=ESCOLARIDADE_CHOICES, null=True, blank=True)
    profissao = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    localTrabalho = models.CharField(max_length=255)
    horarioTrabalho = models.CharField(max_length=100, choices=HORARIO_TRABALHO_CHOICES, null=True, blank=True)

    acolhimento = models.ForeignKey(Acolhimento, on_delete=models.CASCADE, null=True, blank=True, related_name='cadastro', verbose_name='Acolhimento')
    origemDemanda = models.ForeignKey(OrigemDemanda, on_delete=models.CASCADE, null=True, blank=True, related_name='cadastro', verbose_name='Origem de Demanda')
    caracterizacaoMausTratos = models.ForeignKey(CaracterizacaoMausTratos, on_delete=models.CASCADE, null=True, blank=True, related_name='cadastro', verbose_name='Caracterização em caso de maus tratos ou violência')
    denuncianteConduta = models.ForeignKey(DenuncianteConduta, on_delete=models.CASCADE, null=True, blank=True, related_name='cadastro', verbose_name='Denunciante e conduta realizada')
    situacaoHabitacional = models.ForeignKey(SituacaoHabitacional, on_delete=models.CASCADE, null=True, blank=True, related_name='cadastro', verbose_name='Situação habitacional')
    dadosResponsavel = models.ForeignKey(DadosResponsavel, on_delete=models.CASCADE, null=True, blank=True, related_name='cadastro', verbose_name='Dados do Responsável')
    composicaoFamiliar = models.ManyToManyField(ComposicaoFamiliar, blank=True, verbose_name='Composição Familiar')
    
    qmCadastrou = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='cadastros_feitos')
    

    def __str__(self):
        return f'{self.nome} - {self.cpf}'

from django.contrib import admin
from cadastro.models.Cadastro import Cadastro

from cadastro.models.CaracterizacaoMausTratos import CaracterizacaoMausTratos
from cadastro.models.ComposicaoFamiliar import ComposicaoFamiliar
from cadastro.models.DenuncianteConduta import DenuncianteConduta

from cadastro.models.OrigemDemanda import OrigemDemanda
from cadastro.models.SituacaoHabitacional import SituacaoHabitacional

admin.site.register(Cadastro)
admin.site.register(CaracterizacaoMausTratos)
admin.site.register(ComposicaoFamiliar)
admin.site.register(DenuncianteConduta)
admin.site.register(OrigemDemanda)
admin.site.register(SituacaoHabitacional)


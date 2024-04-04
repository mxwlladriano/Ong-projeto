from django.contrib.auth.models import AbstractUser
from django.db import models

UNIDADE_CHOICES = (
    ('crea', 'CREA'),
    ('cras_bairro_da_paz', 'CRAS - Bairro da Paz'),
    ('cras_bairro_panorama', 'CRAS - Bairro Panorama'),
    ('cras_serra_pelada', 'CRAS - Serra Pelada'),
    ('setor_idoso', 'Setor Idoso'),
    ('setor_adolescente', 'Setor Criança/Adolescente'),
)

class Usuario(AbstractUser):
    unidade = models.CharField(max_length=20, choices=UNIDADE_CHOICES, blank=True)
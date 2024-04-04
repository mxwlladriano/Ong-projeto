from django import forms
from cadastro.models import Beneficio

class BeneficioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['qmCadastrou'].required = False        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'p-2 border rounded bg-gray-800 text-white w-full'
    
    class Meta:
        model = Beneficio
        fields = ['nome', 'beneficiado', 'qmCadastrou']

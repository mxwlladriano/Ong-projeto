from django import forms
from cadastro.models import Acolhimento

class AcolhimentoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dataSaida'].required = False
        
        for visible in self.visible_fields():
            fieldType = visible.field.widget.__class__.__name__
            if fieldType == 'DateInput':
                visible.field.widget.attrs['class'] = 'p-2 border rounded bg-gray-800 text-white w-full'
            else:
                visible.field.widget.attrs['class'] = 'p-2 border rounded bg-gray-800 text-white w-full'
                
    class Meta:
        model = Acolhimento
        fields = '__all__'
        widgets = {
            'dataEntrada': forms.DateInput(attrs={'type': 'date'}),
            'dataSaida': forms.DateInput(attrs={'type': 'date'}),
        }

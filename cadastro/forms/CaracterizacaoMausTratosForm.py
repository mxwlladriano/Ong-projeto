from django import forms
from cadastro.models import CaracterizacaoMausTratos

class CaracterizacaoMausTratosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            fieldType = visible.field.widget.__class__.__name__
            if fieldType == 'DateInput':
                visible.field.widget.attrs['class'] = 'p-2 border rounded bg-gray-800 text-white w-full'
            if fieldType == 'TextInput':
                visible.field.widget.attrs['class'] = 'p-2 border rounded bg-gray-800 text-white w-full'
            if fieldType == 'CheckboxSelectMultiple':
                visible.field.widget.attrs['class'] = 'focus:ring-blue-600 ring-offset-gray-800'
         
    class Meta:
        model = CaracterizacaoMausTratos
        fields = '__all__'
        widgets = {
            'caracteristicaAgressaoDataPeriodo': forms.DateInput(attrs={'type': 'date'}),
        }


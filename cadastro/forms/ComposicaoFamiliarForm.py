from django import forms
from cadastro.models import ComposicaoFamiliar

class ComposicaoFamiliarForm(forms.ModelForm):
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
            if fieldType == 'Select' or fieldType== 'NullBooleanSelect' or fieldType== 'NumberInput':
                visible.field.widget.attrs['class'] = 'p-2 border rounded bg-gray-800 text-white w-full'
    class Meta:
        model = ComposicaoFamiliar
        fields = '__all__'


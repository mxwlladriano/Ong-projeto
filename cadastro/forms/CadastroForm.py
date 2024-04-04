from django import forms
from cadastro.models import Cadastro

class CadastroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['numeroProntuario'].required = False
        self.fields['origemDemanda'].required = False
        self.fields['caracterizacaoMausTratos'].required = False
        self.fields['denuncianteConduta'].required = False
        self.fields['situacaoHabitacional'].required = False
        self.fields['dadosResponsavel'].required = False
        self.fields['composicaoFamiliar'].required = False
        self.fields['qmCadastrou'].required = False
        
        for visible in self.visible_fields():
            fieldType = visible.field.widget.__class__.__name__
            if fieldType == 'DateInput':
                visible.field.widget.attrs['class'] = 'p-2 border rounded bg-gray-800 text-white w-full'
            else:
                visible.field.widget.attrs['class'] = 'p-2 border rounded bg-gray-800 text-white w-full'
                
    class Meta:
        model = Cadastro
        fields = '__all__'
        widgets = {
            'dataAtendimento': forms.DateInput(attrs={'type': 'date'}),
            'dataNascimento': forms.DateInput(attrs={'type': 'date'}),
        }

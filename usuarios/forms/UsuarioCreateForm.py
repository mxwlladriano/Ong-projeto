from django.contrib.auth.forms import UserCreationForm
from usuarios.models import Usuario

class UsuarioCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'p-2 border rounded bg-gray-800 text-white w-full'
    
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('username', 'password1', 'password2', 'unidade', 'is_superuser')

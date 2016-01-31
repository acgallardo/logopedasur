from django import forms
from logopedasur.pacientes.models import Pacientes

class PacientesForm(forms.ModelForm):

    '''
    Esto era una prueba del curso, se puede borrar si no es necesario
    def clean_title(self):
        if 'a' in self.cleaned_data['title']:
            raise forms.ValidationError("El campo titulo no puede contener a")
        return self.cleaned_data['title']
    '''

    class Meta:
        model = Pacientes
        fields = '__all__'

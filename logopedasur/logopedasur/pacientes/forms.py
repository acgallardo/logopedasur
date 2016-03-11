from django import forms

from logopedasur.pacientes.models import Paciente, Tutor, Informe

class PacientesForm(forms.ModelForm):

    '''
    Esto era una prueba del curso, se puede borrar si no es necesario
    def clean_title(self):
        if 'a' in self.cleaned_data['title']:
            raise forms.ValidationError("El campo titulo no puede contener a")
        return self.cleaned_data['title']
    '''

    class Meta:
        model = Paciente
        fields = '__all__'


class TutoresForm(forms.ModelForm):

    class Meta:
        model = Tutor
        fields = '__all__'


class NuevoInformeForm(forms.ModelForm):
    '''
        Class that create a form to insert a new report (PDF file)
        to a specific patient
    '''

    class Meta:
        model = Informe
        fields = ('paciente', 'terapeuta', 'tipo', 'fecha_informe', 'fecha_entrega', 'informe')

from django import forms

from logopedasur.sesiones.models import Sesion

class SesionesForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Sesion
        fields = '__all__'

class nuevaSesionForm(forms.ModelForm):
    '''
        Form that show only some fields, for example dont show
        patient (foreign key), because may be preselected automatically
    '''
    class Meta:
        model = Sesion
        fields = ('paciente', 'tipo', 'terapeutas', 'fecha_sesion','hora_inicio', 'hora_fin','observaciones', )

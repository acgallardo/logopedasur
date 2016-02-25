from django import forms

from logopedasur.terapeutas.models import Terapeuta, Especialidad


class TerapeutasForm(forms.ModelForm):

    class Meta:
        model = Terapeuta
        fields = '__all__'


class EspecialidadesForm(forms.ModelForm):

    class Meta:
        model = Especialidad
        fields = '__all__'

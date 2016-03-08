from django import forms

from logopedasur.sesiones.models import Sesion

class SesionesForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Sesion
        fields = '__all__'

from django import forms
from .models import Pan,Empleado

class PanForm(forms.ModelForm):
    class Meta:
        model = Pan
        fields = '__all__'
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
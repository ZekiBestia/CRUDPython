from django import forms
from .models import Pan

class PanForm(forms.ModelForm):
    class Meta:
        model = Pan
        fields = '__all__'
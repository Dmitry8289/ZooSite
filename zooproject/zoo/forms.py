from django.forms import forms, ModelForm
from .models import Zoo


class ZooForm(ModelForm):
    class Meta:
        model = Zoo
        fields = ('animal_type', 'name', 'description')
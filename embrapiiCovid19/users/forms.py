from datetime import date

from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField
from django.core.exceptions import ValidationError

from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={"type": "string"}),
            'born_date': DateInput(attrs={"type": "date"}),
        }
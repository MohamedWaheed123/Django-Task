from datetime import date

from django.forms import ModelForm, TextInput
from django.core.exceptions import ValidationError

from .models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {

            'name': TextInput(attrs={"type": "text"}),
            'email': TextInput(attrs={"type": "email"}),
            'password': TextInput(attrs={"type": "password"})
        }



from django.forms import ModelForm
from .models import Teammate


class TeammateForm(ModelForm):
    class Meta:
        model = Teammate
        fields = ['last_name']
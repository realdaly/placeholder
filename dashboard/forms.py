from django.forms import ModelForm
from frontend.models import *

class GeneralForm(ModelForm):
    class Meta:
        model = General
        fields = "__all__"
from django.forms import ModelForm
from frontend.models import *

class GeneralForm(ModelForm):
    class Meta:
        model = General
        fields = "__all__"


class Social_ItemForm(ModelForm):
    class Meta:
        model = Social_Item
        fields = "__all__"
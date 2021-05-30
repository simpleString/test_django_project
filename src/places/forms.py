from django import forms
from mapwidgets.widgets import GooglePointFieldWidget

from .models import Place


class CreatePlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('title', 'description', 'image', 'coordinate')
        widgets = {
            'coordinate': GooglePointFieldWidget,
        }

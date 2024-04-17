from django.forms import ModelForm
from .models import Caught, Rarity



class CaughtForm(ModelForm):
    class Meta:
        model = Caught
        fields = ['caught']


class RarityForm(ModelForm):
    class Meta:
        model = Rarity
        fields = ['rarity']
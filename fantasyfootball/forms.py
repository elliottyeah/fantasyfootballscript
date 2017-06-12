from django import forms

from .players.models import Player

class SelecterForm(forms.ModelForm):

    class Meta:
        model = Players
        fields = ('player_position', 'buy_value',)
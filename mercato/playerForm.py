from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'rounded-lg'}),
            'first_name': forms.TextInput(attrs={'class': 'rounded-lg'}),
            'age': forms.NumberInput(attrs={'class': 'rounded-lg'}),
            'phone': forms.TextInput(attrs={'class': 'rounded-lg'}),
            'email': forms.EmailInput(attrs={'class': 'rounded-lg'}),
            'gender': forms.Select(attrs={'class': 'rounded-lg'}),
            'country': forms.TextInput(attrs={'class': 'rounded-lg'}),
            'photo' : forms.FileInput(attrs={'class': 'rounded-lg'}),
            'role': forms.RadioSelect(attrs={'class': 'rounded-lg'}),
            'team': forms.Select(attrs={'class': ''}),
        }
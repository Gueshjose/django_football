from django import forms 
from .models import Team,Continent

class TeamForm(forms.ModelForm):
    COMPOSITION_CHOICES = [
        ('F', 'Féminine'),
        ('M', 'Masculine'),
        ('X', 'Mixte'),
    ]
    continent = forms.ModelChoiceField( queryset=Continent.objects.all(),
        to_field_name='id', widget=forms.Select(attrs={'class':"z-1 block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring"}))
    composition = forms.ChoiceField(widget=forms.Select(attrs={'class': 'z-1 block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring'}),choices=COMPOSITION_CHOICES)
    
    class Meta:
        model = Team
        fields = '__all__'
        exclude = ['maxATT', 'maxMID', 'maxDEF', 'maxG','maxRem','composition']
        widgets={
            'name':forms.TextInput(attrs={'class':' z-1 block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring'}),
            'ville':forms.TextInput(attrs={'class':'z-1 block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring'}),
            'pays':forms.TextInput(attrs={'class':' z-1 block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring'}),
            'maxREM':forms.NumberInput(attrs={'min':0,'max':10,'class':'z-1 block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring'}),
        }
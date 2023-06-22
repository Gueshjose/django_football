from django import forms 
from .models import Team,Continent

class TeamForm(forms.ModelForm):
    continent = forms.ModelChoiceField( queryset=Continent.objects.all(),
        to_field_name='id', widget=forms.Select(attrs={'class':"z-1 block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring"}))
    
    class Meta:
        model = Team
        fields = '__all__'
        exclude = ['maxATT', 'maxMID', 'maxDEF', 'maxG']
        widgets={
            'name':forms.TextInput(attrs={'class':' z-1 block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring'}),
            'ville':forms.TextInput(attrs={'class':'z-1 block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring'}),
            'pays':forms.TextInput(attrs={'class':' z-1 block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring'}),
            'maxREM':forms.NumberInput(attrs={'min':0,'max':10,'class':'z-1 block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring'}),
        }
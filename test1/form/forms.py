from .models import Forms
from django.forms import ModelForm, TextInput, Textarea, DateInput

class FormsForm(ModelForm):
    class Meta:
        model = Forms
        fields = ['name', 'sourname', 'age', 'comment']

        widgets = {
            'name': TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Имя'
            }),
            'sourname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            'age': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения'
            }),
            'comment': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'О себе'
            })
        }
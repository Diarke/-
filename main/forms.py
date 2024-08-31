from .models import Quizz
from django.forms import ModelForm, Textarea, TextInput


class QuizForm(ModelForm):
    class Meta:
        model = Quizz
        fields = ['title', 'url']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Игра, класс, предмет'
            }),
            "url": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'iframe'
            })
        }
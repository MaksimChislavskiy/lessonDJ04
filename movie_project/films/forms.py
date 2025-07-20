from .models import Film
from django.forms import ModelForm, TextInput, Textarea


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'comments']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание фильма'}),
            'comments': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзывы'}),
        }

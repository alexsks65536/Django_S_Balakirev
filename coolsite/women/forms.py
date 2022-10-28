from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Women
        # fields = '__all__' # список ВСЕХ полей формы
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']  # список полей формы, которые выводятся
        # виджеты с классами для полей
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form_settings input'}),
            'content': forms.Textarea(attrs={'class': 'form_settings textarea', 'cols': 70, 'rows': 12}),  #
        }

    def clean_title(self):
        """
        Валидатор формы
        """
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title
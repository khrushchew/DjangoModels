from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    # можно и так
    # text = forms.CharField(min_length=300)

    class Meta:
        model = Post
       # fields = '__all__'

        fields = [
            'author',
            'title',
            'text',
            'categories'
        ]

    def clean(self):
        cleaned_data = super().clean()

        text = cleaned_data.get("text")
        if text is not None and len(text) < 100:
            raise ValidationError("Текст не может быть менее 100 символов."
            )

        # название статьи не должно стоять в самом начале текста
        title = cleaned_data.get("title")
        len_title = len(title)
        if title[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы.")

        elif title.lower() == text[:len_title].lower():
            raise ValidationError(
                "Небольшая ошибка: название статьи не должно стоять в самом начале текста. Попробуйте ещё раз"
            )

        return cleaned_data

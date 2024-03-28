from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class NewsForm(forms.ModelForm):
   text = forms.CharField(min_length=5)
   class Meta:
       model = Post
       fields = [
          'title',
          'text',
          'author',
       ]

   def clean(self):
      cleaned_data = super().clean()
      text = cleaned_data.get("text")
      title = cleaned_data.get("title")

      if title == text:
         raise ValidationError(
            "Описание не должно быть идентично названию."
         )

      return cleaned_data


class ArticlesForm(forms.ModelForm):
   text = forms.CharField(min_length=5)
   class Meta:
       model = Post
       fields = [
          'title',
          'text',
          'author',
       ]

   def clean(self):
      cleaned_data = super().clean()
      text = cleaned_data.get("text")
      title = cleaned_data.get("title")

      if title == text:
         raise ValidationError(
            "Описание не должно быть идентично названию."
         )

      return cleaned_data
from django_filters import FilterSet, ModelChoiceFilter
from .models import Post, Author

class AuthorFilter(FilterSet):
    class Meta:
        model = Author
        fields = {
            'name': ['icontains'],
        }

class NewsFilter(FilterSet):
    author = ModelChoiceFilter(field_name='author__name', queryset=Author.objects.all())

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'created_at': ['gt']
        }

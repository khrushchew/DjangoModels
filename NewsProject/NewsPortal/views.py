from django.views.generic import ListView, DetailView
from .models import Post

class NewsListView(ListView):
    model = Post
    ordering = '-created_at'

    template_name = 'news.html'

    context_object_name = 'posts'

class NewsDetail(DetailView):
    model = Post

    template_name = 'post.html'

    context_object_name = 'post'

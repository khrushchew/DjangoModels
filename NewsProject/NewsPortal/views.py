from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import NewsFilter
from .forms import NewsForm, ArticlesForm
from django.urls import reverse_lazy

class NewsListView(ListView):
    model = Post
    ordering = '-created_at'

    template_name = 'news_search.html'

    context_object_name = 'posts'

    paginate_by = 10

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = NewsFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context

class NewsDetail(DetailView):
    model = Post

    template_name = 'post.html'

    context_object_name = 'post'

class View(ListView):
    model = Post
    ordering = '-created_at'

    template_name = 'news.html'

    context_object_name = 'posts'

# Добавляем новое представление для создания товаров.
class NewsCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = NewsForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'Новость'
        return super().form_valid(form)


# Добавляем представление для изменения товара.
class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'Новость'
        return super().form_valid(form)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.post_type == "Статья":
            raise Http404("Статьи нельзя изменять через эту страницу")
        return obj


# Представление удаляющее товар.
class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_search')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'Новость'
        return super().form_valid(form)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.post_type == "Статья":
            raise Http404("Статьи нельзя удалять через эту страницу")
        return obj



class ArticlesCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = ArticlesForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'articles_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'Статья'
        return super().form_valid(form)


# Добавляем представление для изменения товара.
class ArticlesUpdate(UpdateView):
    form_class = ArticlesForm
    model = Post
    template_name = 'articles_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'Статья'
        return super().form_valid(form)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.post_type == "Новость":
            raise Http404("Новости нельзя изменять через эту страницу")
        return obj

# Представление удаляющее товар.
class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('news_search')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'Статья'
        return super().form_valid(form)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.post_type == "Новость":
            raise Http404("Новости нельзя удалять через эту страницу")
        return obj
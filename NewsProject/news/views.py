from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Post, User, Category, SubscriptionsCategory, PostCategory
from .filters import PostFilter
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.core.mail import send_mail, mail_admins
from django.db.models.signals import post_save
from django.dispatch import receiver





class NewsList(ListView, PermissionRequiredMixin):
    permission_required = ('news.view_post', )
    model = Post
    ordering = '-date_time_creation_post'
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return queryset.filter(post_or_news='NEWS')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class NewsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post', 'news.view_post',
                          )
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_or_news = 'NEWS'
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     message = Post(
    #         title=request.POST['title'],
    #         text=request.POST['text'],
    #         # date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
    #         # client_name=request.POST['client_name'],
    #         # message=request.POST['message'],
    #     )
    #     message.save()
    #
    #     # отправляем письмо
    #     send_mail(
    #         subject=message.title,
    #         # имя клиента и дата записи будут в теме для удобства
    #         message=message.text,  # сообщение с кратким описанием проблемы
    #         from_email='starschinowa.anastasia@yandex.ru',  # здесь указываете почту, с которой будете отправлять (об этом попозже)
    #         recipient_list=['starschinowa.ana@gmail.com', ]  # здесь список получателей. Например, секретарь, сам врач и т. д.
    #     )
    #
    #     return redirect('/')


class NewsEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post', 'news.view_post',
                           )
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


class NewsDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post', 'news.view_post',
                           )
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')


class ArticlesList(ListView, PermissionRequiredMixin):
    permission_required = ('news.view_post',)
    model = Post
    ordering = '-date_time_creation_post'
    template_name = 'articles.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return queryset.filter(post_or_news='POST')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class ArticlesCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):

    permission_required = ('news.add_post', 'news.view_post',
                           )
    form_class = PostForm
    model = Post
    template_name = 'articles_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_or_news = 'POST'
        return super().form_valid(form)


class ArticlesEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post', 'news.view_post',
                           )
    form_class = PostForm
    model = Post
    template_name = 'articles_edit.html'


class ArticlesDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post', 'news.view_post',
                           )
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('post_list')


class PostSearch(ListView):
    # Указываем нашу разработанную форму
    form_class = PostForm
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        # context['time_now'] = datetime.now()
        context['filterset'] = self.filterset
        context['next_sale'] = None
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset()
        self.category_id = [elem.get('id') for elem in Post.objects.get(id=self.kwargs['pk']).categories.values('id')]
        if len(self.category_id) == 1:
            self.category_id = [elem.get('id') for elem in Post.objects.get(id=self.kwargs['pk']).categories.values('id')][0]
        else:
            pass
        print(f'self.category_id = {self.category_id}')
        # self.category_and_users = [elem for elem in SubscriptionsCategory.objects.filter(category=self.category_id).values('user', 'category')]
        # print(f'self.category_and_users = {self.category_and_users}')
        # if len(self.category_and_users) == 1:
        #     self.user = self.category_and_users[0].get('user')
        #     print(f'self.user = {self.user}')
        # else:
        #     self.user = [elem.get('user') for elem in self.category_and_users]
        #     print(f'self.user = {self.user}')
        self.users = [elem for elem in SubscriptionsCategory.objects.filter(category=self.category_id).values('user')]
        print(f'self.users = {self.users}')
        if len(self.users) == 1:
            self.users = self.users[0].get('user')
            print(f'self.users = {self.users}')
        else:
            self.users = [elem.get('user') for elem in self.users]
            print(f'self.users = {self.users}')


        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        if type(self.users) == int:
            context['is_subscriber'] = True if self.request.user.id == self.users else False
        else:
            context['is_subscriber'] = True if self.request.user.id in self.users else False
        print(f"context['is_subscriber'] = {context['is_subscriber']}")
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(pk=pk)
    user.subscriptions.add(category)


    context = {'category': category}
    send_mail(
        subject=f'{user.username}, вы подписались на категорию: {category}',
        # имя клиента и дата записи будут в теме для удобства
        message='Вы подписались на категорию: ',  # сообщение с кратким описанием проблемы
        from_email='starschinowa.anastasia@yandex.ru',  # здесь указываете почту, с которой будете отправлять (об этом попозже)
        recipient_list=[user.email, ]  # здесь список получателей. Например, секретарь, сам врач и т. д.
    )

    # return redirect('/main/subscribe/notification')
    return render(request, 'subscription_notification.html', context=context)

    # message = 'Вы успещно подписались на категорию'
    #
    # return render(request, 'subscription_notification.html', {'category': category, 'message': message})


@login_required
def unsubscribe(request, pk):
    user = request.user
    category = Category.objects.get(pk=pk)
    user.subscriptions.remove(category)
    context = {'category': category}
    send_mail(
        subject=f'{user.username}, вы отписались от категории: {category}',
        # имя клиента и дата записи будут в теме для удобства
        message=f'{user.username}, вы отписались от категории: {category}',  # сообщение с кратким описанием проблемы
        from_email='starschinowa.anastasia@yandex.ru',  # здесь указываете почту, с которой будете отправлять (об этом попозже)
        recipient_list=[user.email, ]  # здесь список получателей. Например, секретарь, сам врач и т. д.
    )

    return render(request, 'unsubscription_notification.html', context=context)


# class CategoryListView(ListView):
#     model = Post
#     template_name = 'category_list.html'
#     context_object_name = 'categories_list'
#
#     def get_queryset(self):
#         self.users = get_object_or_404(User, id=self.kwargs['pk'])
#         queryset = Post.objects.filter(categories=self.category).order_by('-date_time_creation_post')
#         return queryset
#
#     # def get_queryset(self):
#     #     self.category = get_object_or_404(Category, id=self.kwargs['pk'])
#     #     queryset = Post.objects.filter(categories=self.category).order_by('-date_time_creation_post')
#     #     return queryset
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['is_not_subscriber'] = self.request.user not in self.users.subscriptions.all()
#         # context['category'] = self.category
#         context['users'] = self.users
#         return context




    # class NewsList(ListView, PermissionRequiredMixin):
    #     permission_required = ('news.view_post',)
    #     model = Post
    #     ordering = '-date_time_creation_post'
    #     template_name = 'news.html'
    #     context_object_name = 'posts'
    #     paginate_by = 3
    #
    #     def get_queryset(self):
    #         queryset = super().get_queryset()
    #         self.filterset = PostFilter(self.request.GET, queryset)
    #         return queryset.filter(post_or_news='NEWS')
    #
    #     def get_context_data(self, **kwargs):
    #         context = super().get_context_data(**kwargs)
    #         # Добавляем в контекст объект фильтрации.
    #         context['filterset'] = self.filterset
    #         return context
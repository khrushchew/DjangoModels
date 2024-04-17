from django_filters import FilterSet, ModelMultipleChoiceFilter, NumberFilter, CharFilter, DateFilter
from .models import Post, Category, Author, User


class PostFilter(FilterSet):
    category = ModelMultipleChoiceFilter(field_name='postcategory__category',
                                 queryset=Category.objects.all(),
                                 label='категории')
                                 # empty_label='любая категория')

    author = ModelMultipleChoiceFilter(field_name='author',
                                         queryset=Author.objects.all(),
                                         label='автор')

    # author = ModelMultipleChoiceFilter(field_name='author__user',
    #                                    queryset=User.objects.all(),
    #                                    label='автор')
    # ещё вариант как сделать, чтобы все названия выпадали и можно было выбрать
    # title = ModelMultipleChoiceFilter(field_name='title',
    #                              queryset=Post.objects.all(),
    #                              label='название новости/статьи')

    # title = ModelMultipleChoiceFilter(field_name='title', queryset=Post.objects.all(), label='название новости/статьи')
    #
    # # title_1 = CharFilter(field_name='title', label='ещё один вариант поиска новости/статьи')
    #
    # date_time_creation_post = DateFilter(field_name='date_time_creation_post', label='дата создания поста (позже, чем... введите в формате ДД ММ ГГГГ)', lookup_expr="gte")


    # class Meta:
    #     # В Meta классе мы должны указать Django модель,
    #     # в которой будем фильтровать записи.
    #     model = Post
    #     # В fields мы описываем по каким полям модели
    #     # будет производиться фильтрация.
    #     fields = {
    #         'title': ['icontains'],
    #         'date_time_creation_post': [
    #             # 'lt',  # цена должна быть меньше или равна указанной
    #             'gt',  # цена должна быть больше или равна указанной
    #         ],
    #     }

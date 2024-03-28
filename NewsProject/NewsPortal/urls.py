from django.urls import path
from .views import NewsListView, NewsDetail, NewsCreate, NewsUpdate, NewsDelete, View

urlpatterns = [
    path('', View.as_view()),
    path('search/', NewsListView.as_view(), name='news_search'),  # Исправлено здесь
    path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='product_delete'),
]

# DjangoModels

<<<<<<< Updated upstream
Этот проект представляет собой пример создания приложения Django NewsPortal.

## Инструкции по использованию

1. Установка:
   - Установите Django, если еще этого не сделано:
     ```bash
     pip install django
     ```
   - Клонируйте репозиторий:
     ```bash
     git clone https://github.com/your_username/your_project.git
     ```
   - Перейдите в папку проекта:
     ```bash
     cd your_project
     ```
   - Примените миграции:
     ```bash
     python manage.py migrate
     ```

2. Запуск Django shell:
   - Откройте консоль Django:
     ```bash
     python manage.py shell
     ```

3. Создание, редактирование и удаление объектов:

```python
from django.contrib.auth.models import User
from NewsPortal.models import Author, Category, Post, PostCategory, Comment

# Удаление всех созданных объектов:
Comment.objects.all().delete()
Post.objects.all().delete()
Category.objects.all().delete()
PostCategory.objects.all().delete()
Author.objects.all().delete()
User.objects.all().delete()

# Создание пользователей и объектов модели Author:
user1 = User.objects.create_user('user1')
user2 = User.objects.create_user('user2')
author1 = Author.objects.create(user=user1, rating=0)
author2 = Author.objects.create(user=user2, rating=0)

# Добавление категорий:
=======
python manage.py shell

# Импортируем необходимые модели и функции
from django.contrib.auth.models import User
from NewsPortal.models import Author, Category, Post, PostCategory, Comment

# Удаляем все комментарии
Comment.objects.all().delete()
# Удаляем все статьи
Post.objects.all().delete()
# Удаляем все категории
Category.objects.all().delete()
# Удаляем все связанные с категориями объекты PostCategory
PostCategory.objects.all().delete()
# Удаляем всех авторов
Author.objects.all().delete()
# Удаляем всех пользователей
User.objects.all().delete()

# Создаем двух пользователей
user1 = User.objects.create_user('user1')
user2 = User.objects.create_user('user2')

# Создаем два объекта модели Author, связанные с пользователями
author1 = Author.objects.create(user=user1, rating=0)
author2 = Author.objects.create(user=user2, rating=0)

# Добавляем 4 категории
>>>>>>> Stashed changes
category1 = Category.objects.create(name='Спорт')
category2 = Category.objects.create(name='Политика')
category3 = Category.objects.create(name='Образование')
category4 = Category.objects.create(name='Технологии')

<<<<<<< Updated upstream
# Создание статей и новостей:
=======
# Добавляем 2 статьи и 1 новость
>>>>>>> Stashed changes
post1 = Post.objects.create(author=author1, post_type='Статья', title='Статья 1', text='Текст статьи 1', rating=0)
post2 = Post.objects.create(author=author2, post_type='Статья', title='Статья 2', text='Текст статьи 2', rating=0)
post3 = Post.objects.create(author=author1, post_type='Новость', title='Новость 1', text='Текст новости 1', rating=0)

<<<<<<< Updated upstream
# Присвоение категорий:
=======
# Присваиваем им категории
>>>>>>> Stashed changes
PostCategory.objects.create(post=post1, category=category1)
PostCategory.objects.create(post=post1, category=category2)
PostCategory.objects.create(post=post2, category=category3)
PostCategory.objects.create(post=post3, category=category4)

<<<<<<< Updated upstream
# Создание комментариев:
=======
# Создаем как минимум 4 комментария к разным объектам модели Post
>>>>>>> Stashed changes
comment1 = Comment.objects.create(post=post1, user=user1, text='Комментарий 1', rating=0)
comment2 = Comment.objects.create(post=post2, user=user2, text='Комментарий 2', rating=0)
comment3 = Comment.objects.create(post=post2, user=user1, text='Комментарий 3', rating=0)
comment4 = Comment.objects.create(post=post3, user=user2, text='Комментарий 4', rating=0)

<<<<<<< Updated upstream
# Применение функций like() и dislike():
=======
# Применяем функции like() и dislike() к статьям/новостям и комментариям
>>>>>>> Stashed changes
post1.like()
post2.dislike()
comment1.like()
comment2.dislike()

<<<<<<< Updated upstream
# Обновление рейтингов пользователей:
author1.update_rating()
author2.update_rating()

# Вывод информации о лучшем пользователе:
best_user = Author.objects.all().order_by('-rating').first()
print(f"Лучший пользователь: {best_user.user.username}, Рейтинг: {best_user.rating}")

# Вывод информации о лучшей статье:
best_post = Post.objects.all().order_by('-rating').first()
print(f"Дата: {best_post.created_at}, Автор: {best_post.author.user.username}, Рейтинг: {best_post.rating}, Заголовок: {best_post.title}, Превью: {best_post.preview()}")

# Вывод всех комментариев к этой статье:
comments_to_best_post = Comment.objects.filter(post=best_post)
for comment in comments_to_best_post:
    print(f"Дата: {comment.created_at}, Пользователь: {comment.user.username}, Рейтинг: {comment.rating}, Текст: {comment.text}")
```

## Обновления

### UPD3:
- Добавлена проверка аутентификации в классе-представлении редактирования профиля.
- Выполнены настройки пакета allauth в файле конфигурации для обеспечения аутентификации.
- В файле конфигурации определены адреса для перенаправления на страницу входа в систему и адрес перенаправления после успешного входа.
- Реализован шаблон с формой входа в систему и настроена конфигурация URL.
- Реализован шаблон страницы регистрации пользователей.
- Добавлена возможность регистрации через Google-аккаунт.
- Созданы группы "common" и "authors". Новые пользователи автоматически добавляются в группу "common".
- Добавлена возможность стать автором (быть добавленным в группу "authors").
- Для группы "authors" предоставлены права создания и редактирования объектов модели "Post" (новостей и статей).
- Добавлена проверка прав доступа в классах-представлениях добавления и редактирования новостей и статей.

### UPD2:
- Добавлен постраничный вывод на /news/ - на одной странице было не больше 10 новостей и видны номера лишь ближайших страниц, а также имеется возможность перехода к первой или последней странице.
- Добавлена страница /news/search. На ней должна реализована возможность искать новости по определённым критериям.

### UPD:
- Теперь есть страница с новостями по пути /news, а также фильтр нежелательных слов.
=======
# Обновляем рейтинги пользователей
author1.update_rating()
author2.update_rating()

# Выводим username и рейтинг лучшего пользователя
best_user = Author.objects.all().order_by('-rating').first()
print(f"Лучший пользователь: {best_user.user.username}, Рейтинг: {best_user.rating}")

# Выводим дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи
best_post = Post.objects.all().order_by('-rating').first()
print(f"Дата: {best_post.created_at}, Автор: {best_post.author.user.username}, Рейтинг: {best_post.rating}, Заголовок: {best_post.title}, Превью: {best_post.preview()}")


# Выводим все комментарии к этой статье
comments_to_best_post = Comment.objects.filter(post=best_post)
for comment in comments_to_best_post:
    print(f"Дата: {comment.created_at}, Пользователь: {comment.user.username}, Рейтинг: {comment.rating}, Текст: {comment.text}")
>>>>>>> Stashed changes

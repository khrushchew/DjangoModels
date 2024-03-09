# DjangoModels

1. Откройте консоль Django:

    ```bash
    python manage.py shell
    ```

2. Импортируйте необходимые модели и функции:

    ```python
    from django.contrib.auth.models import User
    from NewsPortal.models import Author, Category, Post, PostCategory, Comment
    ```

3. Удалите все созданные объекты:

    ```python
    Comment.objects.all().delete()
    Post.objects.all().delete()
    Category.objects.all().delete()
    PostCategory.objects.all().delete()
    Author.objects.all().delete()
    User.objects.all().delete()
    ```

4. Создайте двух пользователей и два объекта модели Author:

    ```python
    user1 = User.objects.create_user('user1')
    user2 = User.objects.create_user('user2')

    author1 = Author.objects.create(user=user1, rating=0)
    author2 = Author.objects.create(user=user2, rating=0)
    ```

5. Добавьте 4 категории:

    ```python
    category1 = Category.objects.create(name='Спорт')
    category2 = Category.objects.create(name='Политика')
    category3 = Category.objects.create(name='Образование')
    category4 = Category.objects.create(name='Технологии')
    ```

6. Добавьте 2 статьи и 1 новость:

    ```python
    post1 = Post.objects.create(author=author1, post_type='Статья', title='Статья 1', text='Текст статьи 1', rating=0)
    post2 = Post.objects.create(author=author2, post_type='Статья', title='Статья 2', text='Текст статьи 2', rating=0)
    post3 = Post.objects.create(author=author1, post_type='Новость', title='Новость 1', text='Текст новости 1', rating=0)
    ```

7. Присвойте им категории:

    ```python
    PostCategory.objects.create(post=post1, category=category1)
    PostCategory.objects.create(post=post1, category=category2)
    PostCategory.objects.create(post=post2, category=category3)
    PostCategory.objects.create(post=post3, category=category4)
    ```

8. Создайте как минимум 4 комментария:

    ```python
    comment1 = Comment.objects.create(post=post1, user=user1, text='Комментарий 1', rating=0)
    comment2 = Comment.objects.create(post=post2, user=user2, text='Комментарий 2', rating=0)
    comment3 = Comment.objects.create(post=post2, user=user1, text='Комментарий 3', rating=0)
    comment4 = Comment.objects.create(post=post3, user=user2, text='Комментарий 4', rating=0)
    ```

9. Примените функции like() и dislike():

    ```python
    post1.like()
    post2.dislike()
    comment1.like()
    comment2.dislike()
    ```

10. Обновите рейтинги пользователей:

    ```python
    author1.update_rating()
    author2.update_rating()
    ```

11. Выведите информацию о лучшем пользователе:

    ```python
    best_user = Author.objects.all().order_by('-rating').first()
    print(f"Лучший пользователь: {best_user.user.username}, Рейтинг: {best_user.rating}")
    ```

12. Выведите информацию о лучшей статье:

    ```python
    best_post = Post.objects.all().order_by('-rating').first()
    print(f"Дата: {best_post.created_at}, Автор: {best_post.author.user.username}, Рейтинг: {best_post.rating}, Заголовок: {best_post.title}, Превью: {best_post.preview()}")
    ```

13. Выведите все комментарии к этой статье:

    ```python
    comments_to_best_post = Comment.objects.filter(post=best_post)
    for comment in comments_to_best_post:
        print(f"Дата: {comment.created_at}, Пользователь: {comment.user.username}, Рейтинг: {comment.rating}, Текст: {comment.text}")
    ```

Этот код предоставляет пример создания, редактирования и удаления объектов в вашем приложении Django NewsPortal с использованием моделей и методов.

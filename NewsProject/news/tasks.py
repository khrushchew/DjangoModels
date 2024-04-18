import datetime
from django.utils import timezone
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from celery import shared_task
from .models import Post, Category


@shared_task
def send_notifications(pk):
   post = Post.objects.get(pk=pk)
   categories = post.category.all()
   title = post.head
   text = post.text
   subscribers_emails = []

   for category in categories:
      subscribers_users = category.subscribers.all()
      for sub_user in subscribers_users:
         subscribers_emails.append(sub_user.email)

   html_content = render_to_string(
      'post_created_email.html',
      {

         'text': text,
         'title': title,
         'link': f'{settings.SITE_URL}/news/{pk}'
      }
   )

   msg = EmailMultiAlternatives(
      subject=post.head,
      body='',
      from_email=settings.DEFAULT_FROM_EMAIL,
      to=subscribers_emails,
   )

   msg.attach_alternative(html_content, 'text/html')
   msg.send()


@shared_task
def send_notifications_weekly():
   today = timezone.now()
   last_week = today - datetime.timedelta(days=7)
   posts = Post.objects.filter(time_in__gte=last_week)
   categories = set(posts.values_list('category__category_type', flat=True))
   subscribers = set(Category.objects.filter(category_type__in=categories).values_list('subscribers__email', flat=True))

   html_content = render_to_string(
      'daily_post.html',
      {
         'link': settings.SITE_URL,
         'posts': posts,
      }

   )

   msg = EmailMultiAlternatives(subject='Статьи за неделю',
                                body='',
                                from_email=settings.DEFAULT_FROM_EMAIL,
                                to=subscribers,
                                )

   msg.attach_alternative(html_content, 'text/html')
   msg.send()



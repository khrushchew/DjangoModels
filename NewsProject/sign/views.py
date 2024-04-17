from django.shortcuts import render
from django.contrib.auth import get_user_model


from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm

from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from news.models import Author


@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
        Author.objects.create(user=user)
    return redirect('/')


class BaseRegisterView(CreateView):
    model = get_user_model()
    # model = User
    form_class = BaseRegisterForm
    # success_url = 'main/news/'
    success_url = '/'

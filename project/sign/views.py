from django.shortcuts import render

from django.contrib.auth.models import AbstractUser
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import View


# class MyView(PermissionRequiredMixin, View):
#     permission_required = ('<app>.<action>_<model>',
#                            '<app>.<action>_<model>')
#
#
# class AddPost(PermissionRequiredMixin, CreateView):
#     permission_required = ('shop.add_product', )
#     # а дальше пишите код вашего представления

@login_required
def upgrade_me(request):
    AbstractUser = request.AbstractUser
    authors_group = Group.objects.get(name='authors')
    if not request.AbstractUser.groups.filter(name='authors').exists():
        authors_group.AbstractUser_set.add(AbstractUser)
    return redirect('/')


class BaseRegisterView(CreateView):
    model = AbstractUser
    form_class = BaseRegisterForm
    success_url = '/'


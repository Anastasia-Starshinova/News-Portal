from django.shortcuts import render
from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import Post, Category, Comment


class PostsList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        # context['time_now'] = datetime.now()
        context['next_sale'] = None
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class CategoriesList(ListView):
    model = Category
    ordering = 'news_category'
    template_name = 'categories.html'
    context_object_name = 'categories'


class CommentsList(ListView):
    model = Comment
    ordering = 'comment'
    template_name = 'comments.html'
    context_object_name = 'comments'


class CommentDetail(DetailView):
    model = Comment
    template_name = 'comment.html'
    context_object_name = 'comment'







from django.shortcuts import render
from django.urls import reverse_lazy
from datetime import datetime

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Category, Comment
from .filters import PostFilter
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
# from django.contrib.auth import get_AbstractUser_model
# AbstractUser = get_AbstractUser_model()


from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.mail import send_mail
from datetime import datetime


class NewsList(ListView):
    model = Post
    ordering = '-date_time_creation_post'
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 10

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return queryset.filter(post_or_news='NEWS')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filterset'] = self.filterset
    #     context['next_sale'] = None
    #     return context


class NewsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_author', 'news.view_author', 'news.add_category',
                           'news.view_category', 'news.add_comment', 'news.view_comment',
                           'news.add_post', 'news.change_post', 'news.delete_post',
                           'news.view_post', 'news.add_postcategory', 'news.view_postcategory',
                           'news.change_postcategory', 'news.delete_postcategory',
                           )
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_or_news = 'NEWS'
        return super().form_valid(form)


class NewsEdit(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'



# Представление удаляющее товар.
class NewsDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')


class ArticlesList(ListView):
    model = Post
    ordering = '-date_time_creation_post'
    template_name = 'articles.html'
    context_object_name = 'posts'
    paginate_by = 10

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return queryset.filter(post_or_news='POST')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filterset'] = self.filterset
    #     context['next_sale'] = None
    #     return context


class ArticlesCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_author', 'news.view_author', 'news.add_category',
                           'news.view_category', 'news.add_comment', 'news.view_comment',
                           'news.add_post', 'news.change_post', 'news.delete_post',
                           'news.view_post', 'news.add_postcategory', 'news.view_postcategory',
                           'news.change_postcategory', 'news.delete_postcategory',
                           )
    form_class = PostForm
    model = Post
    template_name = 'articles_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_or_news = 'POST'
        return super().form_valid(form)


# Добавляем представление для изменения товара.
class ArticlesEdit(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'articles_edit.html'


class ArticlesDelete(LoginRequiredMixin, DeleteView):
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


# еще вариант страницы с созданием поста
# def create_post(request):
#     form = PostForm
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/news/')
#     return render(request, 'news_create.html', {'form': form})




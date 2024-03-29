from django_filters import FilterSet, ModelMultipleChoiceFilter, NumberFilter, CharFilter, DateFilter
from .models import Post, Category, Author, User

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.


class PostFilter(FilterSet):
    category = ModelMultipleChoiceFilter(field_name='postcategory__category',
                                 queryset=Category.objects.all(),
                                 label='категории')
                                 # empty_label='любая категория')

    author = ModelMultipleChoiceFilter(field_name='author__user',
                                         queryset=User.objects.all(),
                                         label='автор')

    # ещё вариант как сделать, чтобы все названия выпадали и можно было выбрать
    # title = ModelMultipleChoiceFilter(field_name='title',
    #                              queryset=Post.objects.all(),
    #                              label='название новости/статьи')

    title = ModelMultipleChoiceFilter(field_name='title', queryset=Post.objects.all(), label='название новости/статьи')

    title_1 = CharFilter(field_name='title', label='ещё один вариант поиска новости/статьи')

    date_time_creation_post = DateFilter(field_name='date_time_creation_post', label='дата создания поста (позже, чем... введите в формате ДД ММ ГГГГ)', lookup_expr="gte")


    # release_year = NumberFilter(field_name='date_time_creation_post', lookup_expr='year')
    # release_year__gt = NumberFilter(field_name='date_time_creation_post', lookup_expr='year__gt')
    # release_year__lt = NumberFilter(field_name='date_time_creation_post', lookup_expr='year__lt')
    # title__name = CharFilter(lookup_expr='icontains')


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

    # class Meta:
    #     # В Meta классе мы должны указать Django модель,
    #     # в которой будем фильтровать записи.
    #     model = Post
    #     # В fields мы описываем по каким полям модели
    #     # будет производиться фильтрация.
    #     # fields = {'category', 'author', 'date_time_creation_post': ['gt'], 'title'}
    #     fields = {
    #             # 'title': ['icontains'],
    #             'date_time_creation_post': [
    #                 # 'lt',  # цена должна быть меньше или равна указанной
    #                 'gt',  # цена должна быть больше или равна указанной
    #             ],
    #         }
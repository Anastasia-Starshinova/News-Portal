from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetail, CategoriesList, CommentsList, CommentDetail


urlpatterns = [
   path('news/', PostsList.as_view()),
   path('categories/', CategoriesList.as_view()),
   path('news/<int:pk>', PostDetail.as_view()),
   path('comments/', CommentsList.as_view()),
   path('comments/<int:pk>', CommentDetail.as_view()),
]
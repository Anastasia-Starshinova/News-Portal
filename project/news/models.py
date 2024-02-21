from django.db import models
from datetime import datetime
import time
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

news = 'NEWS'
post = 'POST'

POSITIONS = [
    (news, 'новость'),
    (post, 'статья'),
]


# class AbstractUser(models.Model):
#     username = models.TextField(default='...', help_text='Введите своё Имя и Фамилию. Например: Иван Иванов')
#     password = models.CharField(max_length=128)
#     # last_login = models.DateTimeField(blank=True, null=True)
#     last_login = models.DateTimeField(null=True, auto_now_add=True)
#
#     is_active = True
#
#     def __str__(self):
#         return self.username

class User(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username


# class AbstractBaseUser(models.Model):
#     password = models.CharField(('password'), max_length=128)
#     last_login = models.DateTimeField(('last login'), blank=True, null=True)
#
#     is_active = True
#
#
# class AbstractUser(AbstractBaseUser, PermissionsMixin):
#     """
#     An abstract base class implementing a fully featured User model with
#     admin-compliant permissions.
#
#     Username and password are required. Other fields are optional.
#     """
#     username_validator = UnicodeUsernameValidator()
#
#     username = models.CharField(
#         ('username'),
#         max_length=150,
#         unique=True,
#         help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
#         validators=[username_validator],
#         error_messages={
#             'unique': ("A user with that username already exists."),
#         },
#     )
#     first_name = models.CharField(('first name'), max_length=150, blank=True)
#     last_name = models.CharField(('last name'), max_length=150, blank=True)
#     email = models.EmailField(('email address'), blank=True)
#     is_staff = models.BooleanField(
#         ('staff status'),
#         default=False,
#         help_text=('Designates whether the user can log into this admin site.'),
#     )
#     is_active = models.BooleanField(
#         ('active'),
#         default=True,
#         help_text=(
#             'Designates whether this user should be treated as active. '
#             'Unselect this instead of deleting accounts.'
#         ),
#     )
#     date_joined = models.DateTimeField(('date joined'), default=datetime.now)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ["first_name", "last_name"]
#
#     def __unicode__(self):
#         return self.email
#
#     def __str__(self):
#         return self.username


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    rating = models.FloatField(default=0.0)

    def update_rating(self):
        sum_rating_author_posts = 0
        sum_rating_comments_author_posts = 0
        sum_rating_author_comments = 0

        author_posts = Post.objects.filter(author=self.User.id)
        if len(author_posts) == 1:
            rating_author_post = author_posts.values('rating')
            rating_author_post = int([list(elem.values()) for elem in rating_author_post][0][0])
            sum_rating_author_posts = rating_author_post * 3
        else:
            rating_author_post = author_posts.values('rating')
            rating_author_post = [list(elem.values()) for elem in rating_author_post]
            rating_author_post = [int(elem[0]) for elem in rating_author_post]
            sum_rating_author_posts = sum(rating_author_post) * 3

        author_comments = Comment.objects.filter(user=self.User.id)
        if len(author_comments) == 1:
            rating_author_comments = author_comments.values('rating')
            rating_author_comments = int([list(elem.values()) for elem in rating_author_comments][0][0])
            sum_rating_author_comments = rating_author_comments
        else:
            rating_author_comments = author_comments.values('rating')
            rating_author_comments = [list(elem.values()) for elem in rating_author_comments]
            rating_author_comments = [int(elem[0]) for elem in rating_author_comments]
            sum_rating_author_comments = sum(rating_author_comments)

        id_author_posts = author_posts.values('id')
        id_author_posts = [list(elem.values()) for elem in id_author_posts]
        for id_elem in id_author_posts:
            comments_author_posts = Comment.objects.filter(post=id_elem[0])
            ratings_comments_author_posts = comments_author_posts.values('rating')
            ratings_comments_author_posts = [list(elem.values()) for elem in ratings_comments_author_posts]
            ratings_comments_author_posts = [int(elem[0]) for elem in ratings_comments_author_posts]
            sum_rating_comments_author_posts += sum(ratings_comments_author_posts)

        self.rating = sum_rating_author_posts + sum_rating_comments_author_posts + sum_rating_author_comments
        self.save()

    def __str__(self):
        return self.User.username


class Category(models.Model):
    news_category = models.CharField(default='...', max_length=255, unique=True)

    def __str__(self):
        return self.news_category


class Post(models.Model):
    news = 'NEWS'
    post = 'POST'

    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    post_or_news = models.CharField(max_length=4, choices=POSITIONS, default=news)
    date_time_creation_post = models.DateTimeField(null=True, auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(default='...', max_length=255)
    text = models.TextField(default='...')
    rating = models.FloatField(default=0.0)

    class Meta:
        ordering = ['-date_time_creation_post']

    def edit_time(self):
        self.date_time_creation_post = self.date_time_creation_post.replace(tzinfo=None)
        print(self.date_time_creation_post)
        format_string = "%Y-%m-%d %H:%M"
        self.date_time_creation_post = self.date_time_creation_post.strftime(format_string)
        print(self.date_time_creation_post)
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        text = f"{self.text}"
        len_text = len(text)

        if len_text == 124:
            return text[:]

        elif len_text > 124:
            result = ''
            new_text = text[:125]
            ind = 1
            while ind > 0:
                if new_text[-ind].isalnum():
                    ind += 1
                else:
                    if new_text[-ind] == " ":
                        result = new_text[:-ind] + '...'
                        ind = 0
                    elif not new_text[-ind].isalnum() or new_text[-ind] != " ":
                        result = new_text[:-ind] + '...'
                        ind = 0

            return result

        elif len_text < 124:
            return text[:] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.CharField(default='...', max_length=255)
    date_time_creation_comment = models.DateTimeField(null=True, auto_now_add=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.comment[:30]}'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

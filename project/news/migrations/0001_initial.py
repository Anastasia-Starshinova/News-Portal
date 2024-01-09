# Generated by Django 5.0 on 2023-12-25 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractBaseUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_category', models.CharField(default='...', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_rating', models.FloatField(default=0.0)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.abstractbaseuser')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_or_news', models.CharField(choices=[('NEWS', 'новость'), ('POST', 'статья')], default='NEWS', max_length=4)),
                ('date_time_creation_post', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(default='...', max_length=255, unique=True)),
                ('text', models.TextField(default='...')),
                ('news_rating', models.FloatField(default=0.0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.author')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(default='...', max_length=255)),
                ('date_time_creation_comment', models.DateTimeField(auto_now_add=True, null=True)),
                ('comment_rating', models.FloatField(default=0.0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.abstractbaseuser')),
                ('post_1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.post')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.category')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(through='news.PostCategory', to='news.category'),
        ),
    ]

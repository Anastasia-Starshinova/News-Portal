# Generated by Django 5.0 on 2024-01-26 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_time_creation_post',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
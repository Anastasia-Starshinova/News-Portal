# Generated by Django 5.0 on 2024-01-30 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_time_creation_post']},
        ),
    ]

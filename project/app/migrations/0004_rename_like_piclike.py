# Generated by Django 4.2.3 on 2023-07-25 22:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_remove_picture_likes_like'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='like',
            new_name='piclike',
        ),
    ]
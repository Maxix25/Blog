# Generated by Django 5.0.1 on 2024-02-14 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_remove_profile_user'),
        ('posts', '0007_alter_comment_name_alter_posts_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]

# Generated by Django 3.1.6 on 2021-02-22 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_post_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='comments',
        ),
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
    ]
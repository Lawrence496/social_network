# Generated by Django 3.1.6 on 2021-07-16 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0023_auto_20210621_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='shared_users',
            new_name='shared_user',
        ),
    ]

# Generated by Django 3.1.6 on 2021-07-16 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0025_auto_20210716_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cover_picture',
            field=models.ImageField(default='uploads/cover_photos/index.jpg', upload_to='uploads/cover_photos'),
        ),
    ]

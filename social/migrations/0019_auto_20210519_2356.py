# Generated by Django 3.1.6 on 2021-05-20 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0018_auto_20210519_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cover_picture',
            field=models.ImageField(blank=True, default='uploads/cover_photos/index.jpg', upload_to='uploads/cover_photos'),
        ),
    ]

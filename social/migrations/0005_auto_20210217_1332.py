# Generated by Django 3.1.6 on 2021-02-17 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='uploads/profile_pictures/user.png', upload_to='uploads/profile_pictures'),
        ),
    ]

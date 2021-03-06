# Generated by Django 3.1.6 on 2021-05-28 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0021_auto_20210520_0039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/post_photos')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cover_picture',
            field=models.ImageField(default='uploads/cover_photos/index.jpg', upload_to='uploads/cover_photos'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ManyToManyField(blank=True, to='social.Image'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-10 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_comments_file_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ManyToManyField(to='base.usergroup'),
        ),
    ]

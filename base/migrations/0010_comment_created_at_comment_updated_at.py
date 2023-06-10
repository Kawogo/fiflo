# Generated by Django 4.2.1 on 2023-06-10 09:46

from django.db import migrations, models
import django.utils.timezone



class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_comment_user_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now().isoformat),
            preserve_default=False,
        ),
    ]

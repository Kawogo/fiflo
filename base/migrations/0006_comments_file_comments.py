# Generated by Django 4.2.1 on 2023-06-10 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_file_approved_by_alter_file_approved_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, related_name='comments', to='base.comments'),
        ),
    ]

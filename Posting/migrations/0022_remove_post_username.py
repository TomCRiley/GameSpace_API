# Generated by Django 4.0.4 on 2022-04-19 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posting', '0021_post_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='username',
        ),
    ]

# Generated by Django 4.0.4 on 2022-04-19 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posting', '0005_post_delete_userpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.CharField(default='Default texteroooo!', max_length=500),
            preserve_default=False,
        ),
    ]
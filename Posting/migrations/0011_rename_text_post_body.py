# Generated by Django 4.0.4 on 2022-04-19 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posting', '0010_alter_post_createddate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='body',
        ),
    ]
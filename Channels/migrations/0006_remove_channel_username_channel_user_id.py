# Generated by Django 4.0.4 on 2022-04-19 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Channels', '0005_channel_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='username',
        ),
        migrations.AddField(
            model_name='channel',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Channel_Creator_User_id', to=settings.AUTH_USER_MODEL),
        ),
    ]

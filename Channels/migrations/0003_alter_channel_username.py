# Generated by Django 4.0.4 on 2022-04-19 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Channels', '0002_channel_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Channel_Creator_Username', to=settings.AUTH_USER_MODEL),
        ),
    ]

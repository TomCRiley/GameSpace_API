# Generated by Django 4.0.4 on 2022-04-19 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('image', models.CharField(max_length=200)),
                ('release_date', models.DateField(null=True)),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='developer', to='Channels.developer')),
                ('platform', models.ManyToManyField(related_name='platform', to='Channels.platform')),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=300)),
                ('createdDate', models.DateField(null=True)),
                ('image', models.CharField(max_length=200)),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='developers', to='Channels.developer')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='games', to='Channels.game')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='platforms', to='Channels.platform')),
            ],
        ),
    ]

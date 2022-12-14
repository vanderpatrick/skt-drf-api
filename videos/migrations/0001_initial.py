# Generated by Django 3.2.16 on 2022-12-14 12:11

import cloudinary_storage.storage
import cloudinary_storage.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('video', models.ImageField(blank=True, storage=cloudinary_storage.storage.VideoMediaCloudinaryStorage(), upload_to='videos/', validators=[cloudinary_storage.validators.validate_video])),
                ('Post_location', models.CharField(choices=[('gap', 'Gap'), ('rail', 'Rail'), ('ledge', 'Ledge'), ('ramps', 'Ramps'), ('mini-ramp', 'Mini-Ramp'), ('halfpipe', 'Halfpipe'), ('street', 'Street'), ('park', 'Park'), ('other', 'Other')], default='other', max_length=32)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]

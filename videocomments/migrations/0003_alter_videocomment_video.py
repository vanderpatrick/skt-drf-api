# Generated by Django 3.2.16 on 2022-12-14 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20221214_1252'),
        ('videocomments', '0002_alter_videocomment_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videocomment',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videocomments', to='videos.videos'),
        ),
    ]

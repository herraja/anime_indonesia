# Generated by Django 3.2.18 on 2023-03-15 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_anime_api_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='post_url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

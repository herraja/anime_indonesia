# Generated by Django 4.2.1 on 2023-05-29 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_anime_post_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anime',
            options={'ordering': ['-anime_score']},
        ),
    ]

# Generated by Django 3.2.18 on 2023-03-15 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='api_url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

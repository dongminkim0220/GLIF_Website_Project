# Generated by Django 2.1.5 on 2019-01-21 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_news', '0003_auto_20190121_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='2019-01-21 Daily News Clipping', max_length=50),
        ),
    ]

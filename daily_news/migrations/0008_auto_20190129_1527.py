# Generated by Django 2.1.5 on 2019-01-29 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_news', '0007_auto_20190128_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='20190129 Daily News Clipping', max_length=50),
        ),
    ]

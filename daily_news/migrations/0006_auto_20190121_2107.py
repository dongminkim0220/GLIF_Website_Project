# Generated by Django 2.1.5 on 2019-01-21 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_news', '0005_auto_20190121_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_1_en',
            field=models.CharField(default='title_en', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title_1_kr',
            field=models.CharField(default='title_kr', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title_2_en',
            field=models.CharField(default='title_kr', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title_2_kr',
            field=models.CharField(default='title_kr', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title_3_en',
            field=models.CharField(default='title_kr', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title_3_kr',
            field=models.CharField(default='title_kr', max_length=500),
            preserve_default=False,
        ),
    ]
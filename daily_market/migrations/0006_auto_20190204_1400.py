# Generated by Django 2.1.5 on 2019-02-04 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_market', '0005_auto_20190130_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='20190204 Daily Market Analysis', max_length=50),
        ),
    ]
# Generated by Django 2.1.5 on 2019-02-08 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0043_auto_20190208_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='glifer',
            name='priority',
            field=models.IntegerField(default=1),
        ),
    ]
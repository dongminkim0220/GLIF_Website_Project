# Generated by Django 2.1.5 on 2019-01-14 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20190114_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile_img',
        ),
    ]

# Generated by Django 2.1.5 on 2019-01-14 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190114_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_img',
            field=models.ImageField(default='./static/users/man-user.png', upload_to=''),
        ),
    ]

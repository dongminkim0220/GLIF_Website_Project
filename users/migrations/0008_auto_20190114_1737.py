# Generated by Django 2.1.5 on 2019-01-14 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190114_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_img',
            field=models.FileField(upload_to=''),
        ),
    ]

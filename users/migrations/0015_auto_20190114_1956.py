# Generated by Django 2.1.5 on 2019-01-14 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20190114_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_img',
            field=models.FileField(upload_to='profiles/%Y/%m/%d/'),
        ),
    ]

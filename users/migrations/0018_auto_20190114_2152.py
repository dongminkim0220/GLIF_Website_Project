# Generated by Django 2.1.5 on 2019-01-14 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20190114_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='workplace',
            field=models.CharField(default='', max_length=250),
        ),
    ]

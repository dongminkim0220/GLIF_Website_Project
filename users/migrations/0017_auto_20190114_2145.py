# Generated by Django 2.1.5 on 2019-01-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20190114_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='workplace',
            field=models.CharField(default='working place', max_length=250),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.1.5 on 2019-01-29 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_auto_20190128_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]

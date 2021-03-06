# Generated by Django 2.1.5 on 2019-01-28 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20190128_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='birthdate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.EmailField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='extra',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='futureplan',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='glifmotive',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='grad',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='millitary',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='name_kr',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='stu_id',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='testprep',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='willyou',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

# Generated by Django 2.1.5 on 2019-01-30 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daily_news', '0008_auto_20190129_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='20190130 Daily News Clipping', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Daily_News_Clipping_writer', to='users.Glifer'),
        ),
    ]

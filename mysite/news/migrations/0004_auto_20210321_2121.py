# Generated by Django 3.1.5 on 2021-03-21 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210321_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='bbc_news',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='cbc_news',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='global_news',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 3.2.13 on 2022-06-12 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.1.3 on 2020-12-01 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathAPI', '0002_auto_20201201_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mathhistory',
            name='result',
            field=models.IntegerField(default=0),
        ),
    ]

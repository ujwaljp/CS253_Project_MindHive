# Generated by Django 4.0.3 on 2022-03-19 07:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_alter_content_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 19, 13, 19, 26, 476176), verbose_name='date published'),
        ),
    ]

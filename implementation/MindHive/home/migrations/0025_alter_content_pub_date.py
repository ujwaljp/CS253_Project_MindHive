# Generated by Django 4.0.3 on 2022-03-18 03:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_alter_content_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 18, 9, 5, 9, 9128), verbose_name='date published'),
        ),
    ]

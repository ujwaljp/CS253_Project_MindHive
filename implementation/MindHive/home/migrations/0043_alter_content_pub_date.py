# Generated by Django 4.0.3 on 2022-04-28 17:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_alter_content_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 28, 23, 0, 5, 509036), null=True, verbose_name='date published'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-20 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_alter_content_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 20, 16, 32, 3, 660239), null=True, verbose_name='date published'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-14 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_content_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 14, 23, 25, 19, 657733), verbose_name='date published'),
        ),
    ]

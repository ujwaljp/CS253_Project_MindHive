# Generated by Django 4.0.3 on 2022-03-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_report_report_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='static/media/default.jpg', upload_to='static/media/profile_image'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-21 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_alter_question_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 3.2.3 on 2021-07-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0009_auto_20210725_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='question',
            field=models.TextField(),
        ),
    ]

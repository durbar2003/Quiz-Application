# Generated by Django 3.2.4 on 2021-07-26 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0015_auto_20210726_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='answer1',
            new_name='ans',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='answer2',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='answer3',
        ),
    ]

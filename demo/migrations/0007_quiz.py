# Generated by Django 3.2.3 on 2021-07-25 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0006_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
            ],
        ),
    ]

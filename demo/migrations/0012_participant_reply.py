# Generated by Django 3.2.4 on 2021-07-26 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0011_auto_20210726_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='reply',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='demo.reply'),
            preserve_default=False,
        ),
    ]

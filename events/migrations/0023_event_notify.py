# Generated by Django 2.0.5 on 2018-07-28 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_auto_20180404_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='notify',
            field=models.BooleanField(default=True),
        ),
    ]
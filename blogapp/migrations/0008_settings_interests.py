# Generated by Django 3.1.3 on 2020-11-05 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_auto_20201105_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='interests',
            field=models.TextField(blank=True, max_length=5000),
        ),
    ]

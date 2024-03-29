# Generated by Django 3.1.3 on 2020-11-05 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20201104_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='guthub',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='about',
            field=models.TextField(blank=True, max_length=4000),
        ),
        migrations.AlterField(
            model_name='settings',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='settings',
            name='instagram',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='linkedin',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='settings',
            name='spotify',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='telegram',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='twitter',
            field=models.URLField(blank=True),
        ),
    ]

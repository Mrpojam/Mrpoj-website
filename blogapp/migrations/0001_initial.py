# Generated by Django 3.1.3 on 2020-11-04 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memo', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instutation', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('memo', models.TextField(max_length=4000)),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expirince',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('memo', models.TextField(max_length=4000)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pic', models.ImageField(upload_to='images')),
                ('about', models.TextField(max_length=4000)),
                ('email', models.EmailField(max_length=254)),
                ('twitter', models.URLField()),
                ('instagram', models.URLField()),
                ('telegram', models.URLField()),
                ('spotify', models.URLField()),
                ('linkedin', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memo', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Skills_tools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('thumbnail', models.ImageField(upload_to='images')),
            ],
        ),
    ]
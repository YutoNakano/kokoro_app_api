# Generated by Django 2.2.2 on 2019-06-16 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('comment', models.CharField(max_length=128)),
                ('status', models.BooleanField(default=False)),
                ('image_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('comment', models.CharField(max_length=128)),
                ('status', models.BooleanField(default=False)),
                ('image_url', models.CharField(max_length=200)),
                ('url', models.URLField()),
            ],
        ),
    ]

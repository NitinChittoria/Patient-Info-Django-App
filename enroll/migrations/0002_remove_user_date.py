# Generated by Django 3.1 on 2021-07-30 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date',
        ),
    ]
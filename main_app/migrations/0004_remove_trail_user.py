# Generated by Django 3.2.4 on 2021-07-12 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210712_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trail',
            name='user',
        ),
    ]

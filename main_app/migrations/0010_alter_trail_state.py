# Generated by Django 3.2.5 on 2021-07-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20210714_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='state',
            field=models.CharField(max_length=2),
        ),
    ]

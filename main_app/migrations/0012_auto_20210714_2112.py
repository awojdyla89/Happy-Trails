# Generated by Django 3.2.5 on 2021-07-14 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='amenity',
            name='image',
            field=models.CharField(default='TBD', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]

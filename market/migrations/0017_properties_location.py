# Generated by Django 3.2.9 on 2022-03-13 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0016_remove_properties_image_compressed'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='location',
            field=models.TextField(default='Hyd'),
            preserve_default=False,
        ),
    ]

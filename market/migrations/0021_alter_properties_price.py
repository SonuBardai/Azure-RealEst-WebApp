# Generated by Django 3.2.9 on 2022-04-12 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0020_properties_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='price',
            field=models.IntegerField(),
        ),
    ]

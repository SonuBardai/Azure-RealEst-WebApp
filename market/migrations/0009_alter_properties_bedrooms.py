# Generated by Django 3.2.9 on 2022-03-12 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0008_alter_properties_bedrooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='bedrooms',
            field=models.PositiveIntegerField(),
        ),
    ]

# Generated by Django 3.2.9 on 2022-03-12 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_auto_20220312_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='bedrooms',
            field=models.PositiveIntegerField(max_length=10),
        ),
    ]

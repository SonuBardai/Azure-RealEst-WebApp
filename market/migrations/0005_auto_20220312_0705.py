# Generated by Django 3.2.9 on 2022-03-12 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_auto_20220311_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='image1',
            field=models.ImageField(default='', upload_to='property_pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='properties',
            name='image2',
            field=models.ImageField(blank=True, upload_to='property_pics'),
        ),
        migrations.AddField(
            model_name='properties',
            name='image3',
            field=models.ImageField(blank=True, upload_to='property_pics'),
        ),
        migrations.DeleteModel(
            name='PropertyImage',
        ),
    ]

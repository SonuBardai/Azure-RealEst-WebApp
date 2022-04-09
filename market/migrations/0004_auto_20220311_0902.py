# Generated by Django 3.2.9 on 2022-03-11 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20220311_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='bedrooms',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='property-pics')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.properties')),
            ],
        ),
    ]
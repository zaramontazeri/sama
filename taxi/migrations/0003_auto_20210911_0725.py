# Generated by Django 3.1.1 on 2021-09-11 07:25

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_auto_20210911_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='address_point',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, default=None, null=True, srid=4326),
        ),
    ]
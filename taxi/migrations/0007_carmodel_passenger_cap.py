# Generated by Django 3.1.1 on 2021-10-09 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0006_auto_20211002_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='passenger_cap',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.1 on 2021-09-20 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_auto_20210914_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='part',
            field=models.CharField(max_length=30),
        ),
    ]
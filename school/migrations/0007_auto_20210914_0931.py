# Generated by Django 3.1.1 on 2021-09-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20210914_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('female', 'female'), ('male', 'male')], max_length=8),
        ),
    ]

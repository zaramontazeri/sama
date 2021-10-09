# Generated by Django 3.1.1 on 2021-09-12 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transportation_company', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='installment',
        ),
        migrations.AddField(
            model_name='installment',
            name='contract',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='installment', to='transportation_company.installment'),
            preserve_default=False,
        ),
    ]

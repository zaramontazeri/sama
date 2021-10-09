# Generated by Django 3.1.1 on 2021-09-08 04:06

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('car_color', models.CharField(max_length=30)),
                ('produce_year', models.DateField()),
                ('technical_date', models.DateField()),
                ('insurance_date', models.DateField()),
                ('car_code', models.CharField(max_length=30)),
                ('service_type', models.CharField(max_length=30)),
                ('vin_number', models.CharField(max_length=30)),
                ('chasis_number', models.CharField(max_length=30)),
                ('motor_number', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('type', models.TextField(max_length=100)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('national_code', models.TextField(max_length=100)),
                ('driver_code', models.CharField(max_length=100)),
                ('file_code', models.CharField(max_length=30)),
                ('full_name', models.CharField(max_length=30)),
                ('phones', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('avatar', models.ImageField(upload_to='upload/driver/')),
                ('address', models.TextField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('online', models.BooleanField(default=False)),
                ('licence_grade_code', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('rate', models.IntegerField(default=0)),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(choices=[('female', 'female'), ('male', 'male')], max_length=6)),
                ('is_single', models.BooleanField(default=True)),
                ('certificate_date', models.DateField()),
                ('taxi_licnese_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drivers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('requested', 'requested'), ('started', 'started'), ('in_progress', 'in_progress'), ('completed', 'completed')], default='requested', max_length=20)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('source_address', models.TextField(max_length=100)),
                ('source_point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('destination_address', models.TextField(max_length=100)),
                ('destination_point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('pickup_time', models.DateTimeField()),
                ('dropoff_time', models.DateTimeField()),
                ('service_type', models.CharField(choices=[('school', 'school'), ('one_passenger', 'one_passenger'), ('many_passenger', 'many_passenger')], default='school', max_length=20)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travels', to='taxi.car')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travels', to='taxi.driver')),
                ('travelers', models.ManyToManyField(related_name='travels', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='RegionRadius',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('radius', models.TextField(max_length=100)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regionradiuss', to='taxi.driver')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='RegionPolygon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('polygon', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regionpolygons', to='taxi.driver')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('speed', models.IntegerField()),
                ('travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='taxi.travel')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='car',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='taxi.driver'),
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='taxi.carmodel'),
        ),
    ]
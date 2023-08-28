# Generated by Django 4.2.4 on 2023-08-28 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields
import vendors.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, default='Cool', max_length=20)),
                ('address', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Address',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vend_id', shortuuid.django_fields.ShortUUIDField(alphabet='0123456789abcdefABCDEF', length=10, max_length=20, prefix='vend-', unique=True)),
                ('vendor_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to=vendors.models.user_directory_path)),
                ('description', models.CharField(blank=True, default='Cool', max_length=100)),
                ('rating', models.CharField(blank=True, default='Cool', max_length=100)),
                ('warranty_period', models.PositiveIntegerField()),
                ('response_time', models.CharField(blank=True, default='Cool', max_length=100)),
                ('shipping_time', models.CharField(blank=True, default='Cool', max_length=100)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendors.address')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Vendors',
            },
        ),
    ]

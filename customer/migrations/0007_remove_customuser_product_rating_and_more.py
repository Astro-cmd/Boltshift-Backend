# Generated by Django 4.2.4 on 2023-09-28 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_productimage_remove_image_product_id_and_more'),
        ('customer', '0006_alter_productreview_rev_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='product_rating',
        ),
        migrations.AddField(
            model_name='productreview',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product'),
        ),
        migrations.AddField(
            model_name='productreview',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='review_rating',
            field=models.CharField(choices=[('⭐⭐', 2), ('⭐⭐⭐', 3), ('⭐', 1), ('⭐⭐⭐⭐⭐', 5), ('⭐⭐⭐⭐', 4)], default='------', max_length=50),
        ),
        migrations.AlterField(
            model_name='userpayment',
            name='provider',
            field=models.CharField(default='-----', max_length=100),
        ),
        migrations.CreateModel(
            name='ShoppingSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sess_id', shortuuid.django_fields.ShortUUIDField(alphabet='0123456789abcdefABCDEF', length=10, max_length=15, prefix='session-', unique=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=2)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Shopping Session',
                'verbose_name_plural': 'Shopping Sessions',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', shortuuid.django_fields.ShortUUIDField(alphabet='0123456789abcdefABCDEF', length=10, max_length=15, prefix='cart-', unique=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('session_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.shoppingsession')),
            ],
            options={
                'verbose_name_plural': 'Cart Items',
            },
        ),
    ]

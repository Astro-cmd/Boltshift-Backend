# Generated by Django 4.2.4 on 2023-10-05 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_alter_productreview_review_rating_productorders'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('Male', 'm'), ('Female', 'f')], default='-------', max_length=10),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='apartment_complex',
            field=models.CharField(default='----------', max_length=500),
        ),
        migrations.AlterField(
            model_name='productorders',
            name='status',
            field=models.CharField(choices=[('Ongoing', 'ongoing'), ('Pending', 'pending'), ('Cancelled', 'cancelled'), ('Completed', 'paid')], default='-------', max_length=50),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='review_rating',
            field=models.CharField(choices=[('⭐⭐⭐⭐', 4), ('⭐⭐', 2), ('⭐⭐⭐⭐⭐', 5), ('⭐⭐⭐', 3), ('⭐', 1)], default='------', max_length=50),
        ),
    ]

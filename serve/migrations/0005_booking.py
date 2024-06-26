# Generated by Django 5.0.6 on 2024-06-07 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serve', '0004_car_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

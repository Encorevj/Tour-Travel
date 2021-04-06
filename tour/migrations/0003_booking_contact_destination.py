# Generated by Django 3.1.4 on 2021-03-02 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tour', '0002_auto_20210302_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
                ('price_by_bus', models.CharField(max_length=20, null=True)),
                ('price_by_Train', models.CharField(max_length=20, null=True)),
                ('price_by_Flight', models.CharField(max_length=20, null=True)),
                ('food_price', models.CharField(max_length=20, null=True)),
                ('number_of_person', models.CharField(max_length=20, null=True)),
                ('days', models.CharField(max_length=20, null=True)),
                ('nights', models.CharField(max_length=20, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(max_length=30)),
                ('last_Name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=30)),
                ('Lname', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=20, null=True)),
                ('date', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=30, null=True)),
                ('number', models.CharField(max_length=30, null=True)),
                ('price', models.CharField(max_length=30, null=True)),
                ('used_facility', models.CharField(max_length=30, null=True)),
                ('destination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tour.destination')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 5.1.5 on 2025-01-27 19:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('esc_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('wallet_address', models.CharField(max_length=100)),
                ('total_sales', models.IntegerField(default=0)),
                ('total_purchases', models.IntegerField(default=0)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('verified', models.BooleanField(default=False)),
                ('eco_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='eco_trader', to='esc_user.ecouser')),
            ],
        ),
    ]

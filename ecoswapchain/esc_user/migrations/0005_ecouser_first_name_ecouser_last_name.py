# Generated by Django 5.1.5 on 2025-02-04 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esc_user', '0004_alter_ecouser_options_alter_ecouser_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecouser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='ecouser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

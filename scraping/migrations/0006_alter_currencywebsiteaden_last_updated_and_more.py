# Generated by Django 5.0.6 on 2024-06-26 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0005_alter_goldwebsite_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencywebsiteaden',
            name='last_updated',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='currencywebsitesanaa',
            name='last_updated',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='goldwebsite',
            name='last_updated',
            field=models.CharField(max_length=100),
        ),
    ]

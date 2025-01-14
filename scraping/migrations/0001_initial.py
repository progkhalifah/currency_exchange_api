# Generated by Django 5.0.6 on 2024-06-25 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyWebsiteAden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.URLField()),
                ('currency_name_aden', models.CharField(max_length=100)),
                ('sell_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('change_icon', models.CharField(max_length=100)),
                ('buy_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('last_updated', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'CurrencyWebsiteAden',
                'verbose_name_plural': 'CurrencyWebsiteAden',
                'db_table': 'db_TblCurrencyAden',
            },
        ),
        migrations.CreateModel(
            name='CurrencyWebsiteSanaa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.URLField()),
                ('currency_name_sanaa', models.CharField(max_length=100)),
                ('sell_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('change_icon', models.CharField(max_length=100)),
                ('buy_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('last_updated', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'CurrencyWebsiteSanaa',
                'verbose_name_plural': 'CurrencyWebsiteSanaa',
                'db_table': 'db_TblCurrencySanaa',
            },
        ),
        migrations.CreateModel(
            name='GoldWebsite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.URLField()),
                ('currency_name', models.CharField(max_length=100)),
                ('sell_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('change_icon', models.CharField(max_length=100)),
                ('buy_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('last_updated', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'GoldWebsiteAden',
                'verbose_name_plural': 'GoldWebsiteAden',
                'db_table': 'db_TblGoldAden',
            },
        ),
    ]

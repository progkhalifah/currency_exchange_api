from django.contrib import admin

from scraping.models import *


# Register your models here.
@admin.register(CurrencyWebsiteSanaa)
class CurrencyWebsiteSanaa(admin.ModelAdmin):
    list_display = ('currency_name_sanaa', 'sell_rate', 'buy_rate', 'last_updated', 'created_at', 'updated_at')
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']


@admin.register(CurrencyWebsiteAden)
class CurrencyWebsiteAden(admin.ModelAdmin):
    list_display = ('currency_name_aden', 'sell_rate', 'buy_rate', 'last_updated', 'created_at', 'updated_at')
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']


@admin.register(GoldWebsite)
class GoldWebsite(admin.ModelAdmin):
    list_display = ('gold_name', 'sell_rate', 'buy_rate', 'last_updated', 'created_at', 'updated_at')
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']



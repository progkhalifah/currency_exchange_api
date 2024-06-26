from django.db import models

# Create your models here.


class CurrencyWebsiteSanaa(models.Model):
    icon = models.URLField()
    currency_name_sanaa = models.CharField(max_length=100)
    sell_rate = models.DecimalField(max_digits=10, decimal_places=2)
    change_icon = models.CharField(max_length=100)
    buy_rate = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.currency_name_sanaa

    class Meta:
        db_table = 'db_TblCurrencySanaa'
        verbose_name = 'CurrencyWebsiteSanaa'
        verbose_name_plural = 'CurrencyWebsiteSanaa'


class CurrencyWebsiteAden(models.Model):
    icon = models.URLField()
    currency_name_aden = models.CharField(max_length=100)
    sell_rate = models.DecimalField(max_digits=10, decimal_places=2)
    change_icon = models.CharField(max_length=100)
    buy_rate = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.currency_name_aden

    class Meta:
        db_table = 'db_TblCurrencyAden'
        verbose_name = 'CurrencyWebsiteAden'
        verbose_name_plural = 'CurrencyWebsiteAden'


class GoldWebsite(models.Model):
    icon = models.URLField()
    gold_name = models.CharField(max_length=100)
    sell_rate = models.DecimalField(max_digits=10, decimal_places=2)
    change_icon = models.CharField(max_length=100)
    buy_rate = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.gold_name

    class Meta:
        db_table = 'db_TblGoldWebsite'
        verbose_name = 'GoldWebsite'
        verbose_name_plural = 'GoldWebsite'




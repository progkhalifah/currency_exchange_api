from django.urls import path

from scraping import views

app_name = 'scraping'

urlpatterns = [
    path('getAllCurrency/', views.get_all_scraping, name='getAllCurrency'),
    path('getAllCurrencySanaa/', views.get_all_scraping_sanaa, name='getAllCurrencySanaa'),
    path('getAllCurrencyAden/', views.get_all_scraping_aden, name='getAllCurrencyAden'),
    path('getAllGold/', views.get_all_scraping_gold, name='getAllGold'),
]

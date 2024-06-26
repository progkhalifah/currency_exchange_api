# import requests
# from bs4 import BeautifulSoup
#
#
# def scrape_exchange_sanaa():
#     url = "https://2dec.net/rate.html"
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, "html.parser")
#     table = soup.find('table', class_='table-rate')
#     rows = table.find_all('tr')
#
#     data = []
#
#     for row in rows[2:]:
#         cells = row.find_all('td')
#         currency_data = {
#             'icon': cells[0].find('img')['src'],
#             'currency_name': cells[1].text.strip().encode('utf-8'),
#             'sell_rate': cells[2].text.strip(),
#             'change_icon': cells[3].find('i')['class'],
#             'buy_rate': cells[4].text.strip(),
#             'last_updated': cells[5].text.strip(),
#         }
#         data.append(currency_data)
#
#     return data
import os
from django import setup as django_setup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrapingExchangeCurrency.settings')
django_setup()

import requests
from bs4 import BeautifulSoup

from scraping.models import *


def scrape_exchange_sanaa():
    url = "https://2dec.net/rate.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Find all tables with the specified class
    tables = soup.find_all('table', class_='table-rate')

    if len(tables) < 3:
        raise Exception("The webpage does not contain at least two tables with the specified class.")

    # Function to extract data from a table
    def extract_table_data_sanaa(table):
        rows = table.find_all('tr')
        data = []
        for row in rows[2:]:  # Assuming the first two rows are headers
            cells = row.find_all('td')
            currency_data = {
                'icon': cells[0].find('img')['src'],
                'currency_name_sanaa': cells[1].text.strip().encode('utf-8'),
                'sell_rate': cells[2].text.strip(),
                'change_icon': cells[3].find('i')['class'],
                'buy_rate': cells[4].text.strip(),
                'last_updated': cells[5].text.strip(),
            }
            data.append(currency_data)
        return data

    def extract_table_data_aden(table):
        rows = table.find_all('tr')
        data = []
        for row in rows[2:]:  # Assuming the first two rows are headers
            cells = row.find_all('td')
            currency_data = {
                'icon': cells[0].find('img')['src'],
                'currency_name_aden': cells[1].text.strip().encode('utf-8'),
                'sell_rate': cells[2].text.strip(),
                'change_icon': cells[3].find('i')['class'],
                'buy_rate': cells[4].text.strip(),
                'last_updated': cells[5].text.strip(),
            }
            data.append(currency_data)
        return data

    def extract_table_data_gold(table):
        rows = table.find_all('tr')
        data = []
        for row in rows[2:]:  # Assuming the first two rows are headers
            cells = row.find_all('td')
            gold_data = {
                'icon': cells[0].find('img')['src'],
                'gold_name': cells[1].text.strip().encode('utf-8'),
                'sell_rate': cells[2].text.strip().replace(',', ''),
                'change_icon': cells[3].find('i')['class'],
                'buy_rate': cells[4].text.strip().replace(',', ''),
                'last_updated': cells[5].text.strip(),
            }
            data.append(gold_data)
        return data

    # Extract data from the first table
    table1_data = extract_table_data_sanaa(tables[0])
    for item in table1_data:
        CurrencyWebsiteSanaa.objects.update_or_create(
            currency_name_sanaa=item['currency_name_sanaa'].decode('utf-8'),
            defaults={
                'icon': item['icon'],
                'sell_rate': item['sell_rate'],
                'change_icon': ' '.join(item['change_icon']),
                'buy_rate': item['buy_rate'],
                'last_updated': item['last_updated']
            }
        )
        print(table1_data)
        print("task completed 1")

    # Extract data from the second table
    table2_data = extract_table_data_aden(tables[1])
    for item in table2_data:
        CurrencyWebsiteAden.objects.update_or_create(
            currency_name_aden=item['currency_name_aden'].decode('utf-8'),
            defaults={
                'icon': item['icon'],
                'sell_rate': item['sell_rate'],
                'change_icon': ' '.join(item['change_icon']),
                'buy_rate': item['buy_rate'],
                'last_updated': item['last_updated']
            }
        )
        print(table2_data)
        print("task completed 2")

    table3_data = extract_table_data_gold(tables[2])
    for item in table3_data:
        GoldWebsite.objects.update_or_create(
            gold_name=item['gold_name'].decode('utf-8'),
            defaults={
                'icon': item['icon'],
                'sell_rate': item['sell_rate'],
                'change_icon': ' '.join(item['change_icon']),
                'buy_rate': item['buy_rate'],
                'last_updated': item['last_updated']
            }
        )
        print(table3_data)
        print("task completed 3")

    return table1_data, table2_data, table3_data

# def scrape_exchange_aden():
#
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, "html.parser")
#     table = soup.find('table', class_='table-rate')
#     rows = table.find_all('tr')
#
#     data = []
#
#     for row in rows[2:]:
#         cells = row.find_all('td')
#         currency_data = {
#             'icon': cells[0].find('img')['src'],
#             'currency_name': cells[1].text.strip().encode('utf-8'),
#             'sell_rate': cells[2].text.strip(),
#             'change_icon': cells[3].find('i')['class'],
#             'buy_rate': cells[4].text.strip(),
#             'last_updated': cells[5].text.strip(),
#         }
#         data.append(currency_data)
#
#     return data
#
#
# def scrape_gold():
#     url = "https://2dec.net/rate.html"
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, "html.parser")
#     table = soup.find('table', class_='table-rate')
#     rows = table.find_all('tr')
#
#     data = []
#
#     for row in rows[2:]:
#         cells = row.find_all('td')
#         currency_data = {
#             'icon': cells[0].find('img')['src'],
#             'currency_name': cells[1].text.strip().encode('utf-8'),
#             'sell_rate': cells[2].text.strip(),
#             'change_icon': cells[3].find('i')['class'],
#             'buy_rate': cells[4].text.strip(),
#             'last_updated': cells[5].text.strip(),
#         }
#         data.append(currency_data)
#
#     return data
#


# def scrape_exchange_rates():
#     url = "https://2dec.net/rate.html"
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, "html.parser")
#     table = soup.find('table', class_='table-rate')
#     rows = table.find_all('tr')
#
#     for row in rows[2:]:
#         cells = row.find_all('td')
#         currency_name = cells[1].text.strip().encode('utf-8')
#         sell_rate = cells[2].text.strip()
#         buy_rate = cells[4].text.strip()
#         last_updated = cells[5].text.strip()
#
#         # Assuming ExchangeRate model exists with fields icon, currency_name, sell_rate, buy_rate, last_updated, updated_at
#         exchange_rate, created = CurrencyWebsite.objects.update_or_create(
#             currency_name=currency_name.decode('utf-8'),
#             defaults={
#                 'icon': cells[0].find('img')['src'],
#                 'sell_rate': sell_rate,
#                 'change_icon': cells[3].find('i')['class'],
#                 'buy_rate': buy_rate,
#                 'last_updated': last_updated,
#                 'updated_at': timezone.now(),  # Current timestamp
#             }
#         )
#
#         if created:
#             print(f"New record added: {currency_name}")
#         else:
#             print(f"Record updated: {currency_name}")
#
#     print("Scraping task completed.")

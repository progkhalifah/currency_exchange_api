# Set up Django environment
import os
from django import setup as django_setup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django_setup()

from datetime import datetime
from time import sleep

from celery import shared_task

from scraping.models import *
from scraping.scrapers import *


@shared_task
def scrape_currency_website():
    scrape_exchange_sanaa()



def every_10_seconds_task():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"<h1>Hello User! Are You There? Current time is {current_time}</h1>"
    print(message)
    return message


def my_task():
    for i in range(11):
        print(i)
        sleep(1)
    return "Task Complete!"

# @shared_task
# def send_mass_emails(recipient):
#     print(recipient)
#     print("Started to sleep")
#     time.sleep(5)
#     print("wake up from sleep")
#     return
#
#
# @shared_task
# def send_scheduled_emails():
#     print("Sending scheduled emails")
#     # Scheduled email sending logic can be added here
#     return "Scheduled emails sent successfully"

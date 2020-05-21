#!/usr/bin/env python3

# Program Name: amazon_price_tracker.py
# Description:  Track pricing changes for any item on Amazon
# Created:      2020-05-20
# Author:       Ricardo Rodrigues
# Website:      https://github.com/ricardorodrigues-ca/amazon-price-tracker

import requests
from requests_html import HTML
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import locale  # for currency conversion and formatting
locale.setlocale(locale.LC_ALL, '')

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path='./chromedriver', options=options)


APP_VERSION = 0.1

#PRODUCT_URL = input("Please type in or paste the web address of the Amazon product page: ")
PRODUCT_URL = "https://www.amazon.ca/Dell-Screen-LED-Lit-Monitor-P2419H/dp/B07F8XZN69"

PRODUCT_TITLE = "#productTitle"
PRODUCT_PRICE = "#priceblock_ourprice"

driver.get(PRODUCT_URL)

body_element = driver.find_element_by_css_selector("body")
html_string = body_element.get_attribute("innerHTML")

# print(html_string)

html_object = HTML(html=html_string)

title = html_object.find(PRODUCT_TITLE, first=True).text
price = html_object.find(PRODUCT_PRICE, first=True).text

print(title)
# remove CDN$ and whitespace from string, then convert to float
price = float(price.replace('CDN$', '').strip())
# print out price with two decimal places
print(locale.format_string('%.2f', price))

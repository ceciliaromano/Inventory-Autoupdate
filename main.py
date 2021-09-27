import os
import time

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Usando ChromeDriver
driver = webdriver.Chrome("C:/Users/Ceci/Documents/Code/Python/SMInventary/chromedriver.exe")
driver.get("https://www.sexshopmayorista.com.ar")

# Encontrando elementos del DOM en página de login
driver.find_element_by_xpath('//*[@id="header"]/div/div[3]/div[1]/button').click()
driver.find_element_by_id('email').send_keys(os.environ.get('SEX_MAY_USER'))
driver.find_element_by_id('pass').send_keys(os.environ.get('SEX_MAY_PASS'))
driver.find_element_by_id('LoginButton').click()

# Accediendo a la hoja de cálculo
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("preciosjuguetes").sheet1

col_codigo = sheet.col_values(1)
col_precio = sheet.col_values(3)
i = 0

# Chequeando que el producto exista y extrayendo su precio en caso de estar
for item in col_codigo:
    search_entry = driver.find_element_by_xpath('//*[@id="q"]')
    search_entry.click()
    search_entry.send_keys(item)
    time.sleep(2)
    search_entry.send_keys(Keys.DOWN + Keys.ENTER)
    i += 1
    try:
        precio = driver.find_element_by_xpath('//*[@id="contenido"]/div/div/div/div[1]/div/div[1]/h2').text
        precio_util = int(precio.strip("$,00 FINAL"))
        print(item, precio_util, type(precio_util))
        sheet.update_cell(i, col_precio, precio_util)
    except:
        pass

# Estableciendo el precio de venta en base al precio de compra
for item in col_precio:
    i += 1
    if int(item) <= 500:
        print(item, type(item))
        sheet.update_cell(i, 4, item * 2)
    elif int(item) > 500 and int(item) <= 1000:
        print(item, type(item))
        sheet.update_cell(i, 4, item * 1.8)
    elif int(item) > 1000 and int(item) <= 1800:
        print(item, type(item))
        sheet.update_cell(i, 4, item * 1.7)
    else:
        print(item, type(item))
        sheet.update_cell(i, 4, item * 1.5)

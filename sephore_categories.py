from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import re


driver = webdriver.Chrome(r'C:\chromedriver_win32\chromedriver.exe')
print("got driver")


base_url = "https://www.sephora.com/"

driver.get("https://www.sephora.com/brand/list.jsp")

print("website")

with open ('estee_brands.csv','r') as estee_brands:
	lines = estee_brands.readlines()
	cat_list=[]
	for url in lines:
		brand_url = base_url + url
		driver.get(brand_url)

		category_buttons = driver.find_elements_by_xpath('//span[@ng-bind-html="trust(cat.name)"]')
		print(category_buttons)

		

		for category in category_buttons:

			cat_list.append(category.text)
	cat_set=set(cat_list)
	print(cat_set)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import re


driver = webdriver.Chrome(r'C:\chromedriver_win32\chromedriver.exe')

driver.get("http://www.beautypackaging.com/heaps/view/3958")

time.sleep(25)

csv_file = open('beauty_companies.csv', 'w')
writer = csv.writer(csv_file)

years = driver.find_elements_by_xpath('//div[@id="topContentsHeapsScroller"]/ul/li/a[@class="contentLinks "]')

# year_links=[]
year_links={}

for year in years:
	year_links[year.text] = year.get_attribute('href')

	# year_links.append(year.get_attribute('href'))

# for year_link in year_links:
# 	driver.get(year_link)
# 	print(year_link)

for key in year_links:
	driver.get(year_links[key])

	

	table = driver.find_elements_by_xpath('//table[@cellpadding="1"]/tbody/tr/td')

	if table == []:
		table = driver.find_elements_by_xpath('//div[@id="showInTextAds"]/a')
		if table == []:
			table = driver.find_elements_by_xpath('//table[@cellpadding="0"]/tbody/tr/td')

	for record in table:
		company = record.text

		print(key)
		print (company)

		company_dict = {}
				
		company_dict['year'] = key
		company_dict['company'] = company
		
		writer.writerow(company_dict.values())

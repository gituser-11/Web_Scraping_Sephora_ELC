from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import re


driver = webdriver.Chrome(r'C:\chromedriver_win32\chromedriver.exe')
#print("got driver")


base_url = "https://www.sephora.com/"

driver.get("https://www.sephora.com/brand/list.jsp")

#print("website")

#category_code = {'Hair' : 'node=1050092', 'Men' : 'node=1050128', 'Shop by Fragrance Family' : 'node=13012942', 'Shaving' : 'node=1050130', 'Skincare' : 'node=1050055', 
				# 'Perfume' : 'node=1050074', 'Fresh' : 'node=13012944', 'Makeup' : 'node=1050000', 'Women' : 'node=2220514', 'Fragrance' : 'node=1050072', 
				# 'Tools & Brushes' : 'node=1050102', 'Bath & Body' : 'node=1050077', 'Mini Size' : 'node=14267719'}

category_code = {'Hair' : 'node=1050092', 'Men' : 'node=1050128', 'Skincare' : 'node=1050055', 'Makeup' : 'node=1050000', 'Fragrance' : 'node=1050072', 
				'Tools & Brushes' : 'node=1050102', 'Bath & Body' : 'node=1050077'}

csv_file = open('estee.csv', 'w')
writer = csv.writer(csv_file)

with open ('estee_brands.csv','r') as estee_brands:
	lines = estee_brands.readlines()
	for url in lines:
		brand_url = base_url + url
		driver.get(brand_url)

		for category in category_code.keys():
			
			cat_code = (category_code[category])

			category_url = brand_url + '?' + cat_code

			driver.get(category_url)

			#category.click()
			time.sleep(1)

			#url_cat = driver.current_url
			#print(url_cat)

			wait_review = WebDriverWait(driver, 0)  #wait upto 10 sec
			Show_hide = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,
												'//div[@ng-show="hasResults"]')))[0]

			Products = Show_hide.find_elements_by_xpath('.//a[@class="u-size1of4 SkuItem SkuItem--135 SkuItem SkuItem--135"]')
			# print([i.text for i in Products])

			links= []
			for i in Products:
				links.append(i.get_attribute('href'))

			for product in links:
				
				driver.get(product)

				time.sleep(3)
	
				try:

					product_name=driver.find_element_by_xpath('//span[@class="css-1g2jq23"]').text

				except:
					product_name = 'a'

				try:	
					product_size=driver.find_element_by_xpath('//div[@class="css-1mo4r9x"]').text

				except:
					product_size = 'b'

				try:
					product_price=driver.find_element_by_xpath('//div[@class="css-18suhml"]').text.strip()

				except:
					product_price = 'c'

				try:
					product_love=driver.find_element_by_xpath('//span[@data-comp="ProductLovesCount"]').text

				except:
					product_love = 'NA'

				try:
					perfume_size=driver.find_element_by_xpath('//div[@class="css-1o1r7cl"]').text

				except:
					perfume_size = 'NA'

				driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				print("scrolled down")
				time.sleep(1)

				driver.execute_script("window.scrollBy(0, -900);")
				print("scrolled up")
				time.sleep(8)
						
				try:
					product_reviews_complete=driver.find_element_by_xpath('.//span[@class="css-1hc0l1g"]').text
				except:	
					product_reviews_complete = 'e'

				try:
					product_rating=driver.find_element_by_xpath('.//div[@class="css-135rruq"]').text[0:3]
				except:
					product_rating = 'f'

				print(brand_url)
				print(category)
				print(product_name)
				print(product_size)
				print(product_price)
				print(product_love)
				print(perfume_size)
				print(product_reviews_complete)
				print(product_rating)
				

				review_dict = {}
				
				review_dict['brand'] = url
				review_dict['category'] = category
				review_dict['product_name'] = product_name
				review_dict['product_size'] = product_size
				review_dict['product_price'] = product_price
				review_dict['product_love'] = product_love
				review_dict['perfume_size'] = perfume_size
				review_dict['reviews_count'] = product_reviews_complete
				review_dict['product_rating'] = product_rating
				
				writer.writerow(review_dict.values())

				

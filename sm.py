from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
import time
url="https://ncov2019.live/data"
with webdriver.Firefox() as driver:
	wait=WebDriverWait(driver,10)
	driver.get(url)
	time.sleep(10)#wait.until(...)
	cl=driver.find_element_by_css_selector=("#sortable_table_world > tbody > tr:nth-child(1) > td.text--green.text--green.sorting_1")
	print(cl.content)

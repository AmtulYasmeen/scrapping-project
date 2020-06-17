# -------------------fetch fields froma website using a website url--------------------------------------------
# import libraries--- 
# to fetch webpage ---urllib, requests,to parse html webpage----bs4 n lxml 
# to use regular expression---re, to read from csv and write to csv ---csv and pandas.
# to automate the procedure of opening a website and achieving a task (eg. scrapping website/ logging into a webite)---Selenium(python)

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests,re
import bs4 as bs
import csv
import lxml
# path to identify selenium chrome drive in your system
path_to_chrome = 'C:/anaconda/chromedriver_win32/chromedriver'
# open a website using selenium webdrive
browser=webdriver.Chrome(executable_path = path_to_chrome)
# create variables to store the fetched data in list and dictionary
angel_all={}
comp_location=[]
gov_industry=[]
# url='http://www.morningstar.com/stocks/xnas/msft/quote.html'
i=0
# open a webpage using selenium python
browser.get('http://www.morningstar.com/stocks/xnas/msft/quote.html')
# sleep for 3 sec to let the page load
time.sleep(3)
num=20
# j=0
# loop through the more button to display result from all the pages(pagination)
# while num<=400:
# 	try:
# 		more_button=browser.find_element_by_css_selector('div.more')
# 		more_button.click()
# 		time.sleep(2)
# 	except:
# 		break
# 	num+=20
# to extract the required field, identify specific element locator from the webpage-- using inspect element
# use id/class/css selector/xpath
# use those locators as follows to extact required fields and store them in variables

all_comp_loc=browser.find_elements_by_css_selector('#idFinancialsContent > table > tbody > tr:nth-child(11) > td:nth-child(1)')

# loop through the variables to extract and append them to a variable list

for loc in all_comp_loc:
	# loc_href=(loc.get_attribute('href'))
	loc_text=(loc.text)
	# comp_location.append(loc_href)
	gov_industry.append(loc_text)

# update the list into a dictionary
angel_all.update({'value': gov_industry})
# get the dictionary in a dataframe format using pandas
df= pd.DataFrame(angel_all)
# drop duplicates
df_nod=df.drop_duplicates()
# write the dataframe into csv file
df.to_csv('morningstar.csv', index=False, encoding="UTF-8")
print df_nod
print 'Done!!'
# done!!!!!!!!
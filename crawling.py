# -*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import datetime
import sys
from scrappy import Utilities,STATUS

class Crawling:

	def __init__(self):
		print('start')

	def process_scrappy(self,url):

		now = time.localtime()

		log = str(now.tm_year)+'-'+str(now.tm_mon)+'-'+str(now.tm_mday)+' '+str(now.tm_hour)+':'+str(now.tm_min)

		options = webdriver.ChromeOptions()
		options.add_argument('headless')
		options.add_argument('window-size=1920x1080')
		options.add_argument('disable-gpu')
		options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
		options.add_argument('lang=ko_KR')
		options.add_argument('--log-level=3')
			
		driver = webdriver.Chrome('/Users/lonbehold/Bitbucket/coronastatus/chromedriver', chrome_options=options)
		driver.implicitly_wait(3)
		driver.get('about:blank')
		driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")
		driver.get(url)

		html = driver.page_source
		soup = BeautifulSoup(html, 'html.parser')
		
		for i in range(0,16):
			udate = STATUS.scrappy(soup,i,'udate')
			area = STATUS.scrappy(soup,i,'area')
			digit = STATUS.scrappy(soup,i,'digit')
			yesterday = STATUS.scrappy(soup,i,'yesterday')
			print('[',i,'] ',udate,' ',area,' ',digit,' ',yesterday)
		

	def execute(self):

		try:		
			url = 'http://ncov.mohw.go.kr/'
			
			self.process_scrappy(url)
			
		except Exception as e:
			with open('./error.log','a') as file:
				file.write('{} You got an error: {}\n'.format(datetime.datetime.now().strtime('%Y-%m-%d %H:%M:%S'),str(e)))

def run():
	crawling = Crawling()
	crawling.execute()

if __name__ == "__main__":
	run()

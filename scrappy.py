# -*- coding: utf-8 -*- 
import re
import time
import urllib.request
import os
from datetime import datetime

class STATUS:

	def scrappy(soup,seq,keyword):

		wrap_nj = soup.find('div',{'class':'wrap nj'})
		mainlive_container = wrap_nj.find('div',{'class':'mainlive_container'})
		container = mainlive_container.find('div',{'class':'container'})
		div = container.find_all('div')
		liveboard_layout = div[0].find('div',{'class':'liveboard_layout'})
		live_right = liveboard_layout.find('div',{'class':'live_right'})

		if keyword == 'udate':
			head = live_right.find('h2')
			a = head.find('a')
			livedate  = a.find('span',{'class':'livedate'}).get_text().strip()
			tmp = Utilities.make_array(str(livedate),'(')
			tmp2 = Utilities.make_array(str(tmp[1]),')')			
			value = Utilities.remove_keyword(tmp2[0])
		elif keyword == 'area':
			main_maparea = live_right.find('div',{'class':'main_maparea'})
			hasSVG = main_maparea.find('div',{'class':'hasSVG'})
			button = hasSVG.find_all('button')
			area = button[seq].find('span',{'class':'name'}).get_text().strip()
			value = area
		elif keyword == 'digit':
			main_maparea = live_right.find('div',{'class':'main_maparea'})
			hasSVG = main_maparea.find('div',{'class':'hasSVG'})
			button = hasSVG.find_all('button')
			digit = button[seq].find('span',{'class':'num'}).get_text().strip()
			value = digit
		elif keyword == 'yesterday':
			main_maparea = live_right.find('div',{'class':'main_maparea'})
			hasSVG = main_maparea.find('div',{'class':'hasSVG'})
			button = hasSVG.find_all('button')
			before = button[seq].find('span',{'class':'before'}).get_text().strip()
			value = before					
		return value		

class Utilities:

	def make_array(string,keyword): 
		arr = []
		arr = string.split(keyword)
		return arr

	def remove_certaion_tag(string):
		string = re.sub('<span.*?>.*?</span>', '', str(string), 0, re.I|re.S)
		return string

	def remove_all_tag(string):
		string = re.sub('<[^<]+?>', '', string)
		return string

	def remove_keyword(string):
		string = string.replace('>', '')
		string = string.replace('\'', '')
		string = string.replace(',', '')
		return string		

	def tokenize(string, token):
		arr = []
		arr = string.split(token)
		return arr
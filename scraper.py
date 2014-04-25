import json
import requests
from bs4 import BeautifulSoup
import cProfile
from collections import OrderedDict

class Scraper(object):
	
	def __init__(self):
		self.__proxies = {
			'http':'http://23.27.197.200:24801',
			'http':'http://23.27.197.201:24801',
			'http':'http://23.27.197.202:24801',
			'http':'http://23.27.197.203:24801',
			'http':'http://23.27.197.204:24801',
			'http':'http://23.27.197.205:24801',
		}
		self.__base_url = 'http://cebu.mynimo.com/'
		self.__base_page = 1
		self.__base_search_types = {
			'jobs':'jobs',
			'overseas':'overseas',
			'high-school-jobs':'high-school-jobs',
			'part-time-jobs':'part-time-jobs'
		}
	
	def get_data(self, keywords, **kwargs):
		self.results = 0
		search_types = self.__determine_search_type(kwargs)			
		for keyword in keywords:
			for search_type in search_types:
				page = 1
				self.__url = self.__generate_url(keyword, search_type, page)
				while self.__has_results(self.__url):					
					self.__extract_data(keyword, self.__url)
					print self.__url.url, self.results
					page += 1
					self.__url = self.__generate_url(keyword, search_type, page)
	
	def __determine_search_type(self, args):

		search_types = {self.__base_search_types['jobs']}
		if not args:
			search_types = {self.__base_search_types['jobs']}
		elif 'all' in args.values():
			print '>> all'
			search_types = self.__base_search_types
		else:
			if args['search_type'] in self.__base_search_types.keys():
				search_types = {self.__base_search_types[args['search_type']]}
			else:
				search_types = {self.__base_search_types['jobs']}
		return search_types
	
	def __generate_url(self, keyword, search_type, page):
		payload = {'q':keyword, 'searchType': search_type, 'page':page}
		r = requests.get(self.__base_url + search_type + '/search/', proxies = self.__proxies, params=payload)
		r.encoding = 'utf-8'
		return r
	
	def __has_results(self, url):
		has_results = True
		soup = BeautifulSoup(url.text)
		no_results_div = soup.find_all('div', {'class', 'no_entries'})
		if len(no_results_div) >= 1:
			has_results = False
		else:
			has_results = True
		return has_results
	
	def __extract_data(self, keyword, url):
		soup = BeautifulSoup(url.text)
		for tr in soup.find_all('tr', {'class', 'aJobS'}):
			data = OrderedDict()
			data['keyword'] = keyword
			details = tr.findAll('td', {'class', 'search_highlight'})
			data['job_title'] = self.__sanitize(details[0].find('a', {'class':'jobTitleLink'}).text.encode('utf-8'))
			location = ''
			preceded = False
			if details[1].span:
				location += details[1].span.text
				preceded = True
			if details[1].contents[0]:
				if preceded:
					location += ',' + details[1].contents[0].string
				else:
					location += details[1].contents[0].string
			data['location'] = self.__sanitize(location)
			data['company'] = self.__sanitize(details[2].text.encode('utf-8'))
			data['short_description'] = self.__sanitize(tr.find_next_sibling('tr').find('div', {'class':'searchContent'}).text.encode('utf-8'))
			self.__save_to_file(data)
			self.results+=1
	
	def __save_to_file(self, data):
		with open('result.json', 'a') as f:
			f.write("{},\n".format(json.dumps(data, indent=4)))
			f.close
	
	def __sanitize(self, string):
		return ' '.join(string.split())

if __name__ == '__main__':
	keywords = ['java']
	
	scraper = Scraper()
	scraper.get_data(keywords)
	
	#~ scraper.get_data(keywords, search_type='part-time-jobs')
	#~ scraper.get_data(keywords, search_type='all')
	
	#~ cProfile.run("scraper.get_data(keywords)")

import cProfile
import json
import requests
from bs4 import BeautifulSoup

class Scraper(object):
	def __init__(self):
		self.__base_payload = payload = {'q':' ', 'searchType':'jobs', 'page':1}
		self.__base_request = requests.get('http://cebu.mynimo.com/jobs/search/?', params=payload)

	def search(self, keywords=['java']):		
		page = pages = 1

		for keyword in keywords:
			
			''' Visit page once and get number of pages. '''
			payload = {'q':keyword, 'searchType':'jobs', 'page':page}
			r = requests.get('http://cebu.mynimo.com/jobs/search/?', params=payload)
			r.encoding = 'utf-8'
			soup = BeautifulSoup(r.text)
			pages = self.__get_pages(soup)

			for page in xrange(1, pages+1):
				print '>>>', keyword, page
				try: 
					payload = {'q':keyword, 'searchType':'jobs', 'page':page}
					r = requests.get('http://cebu.mynimo.com/jobs/search/?', params=payload)
					r.encoding = 'utf-8'
					soup = BeautifulSoup(r.text)
					self.__extract_data(soup, keyword)
				except requests.ConnectionError as conn_err:
					print conn_err
				except requests.RequestException as req_err:
					print req_err
				except requests.HTTPError as http_err:
					print http_err

	def __get_pages(self, soup):
		paginator = soup.find('ul', {'class':'paginator'})
		try:
			for child in paginator.findChildren('li'):
				if child.text.isdigit(): pages = child.text
		except:
			pages = 1
		return int(pages)

	def __extract_data(self, soup, keyword):
		with open('result.json', 'a') as f:
			for tr in soup.find_all('tr', {'class', 'aJobS'}):
				data = {}
				data['keyword'] = keyword
				details = tr.findAll('td', {'class', 'search_highlight'})
				#~ print details[0].div.a.text.encode('utf-8').strip()
				#~ print details[1].text.encode('utf-8').strip()
				#~ print details[2].text.encode('utf-8').strip()
				#~ print tr.find_next_sibling('tr').td.div.div.text.encode('utf-8').strip()
				#~ print '===================================='
				data['job_title'] = details[0].div.a.text.encode('utf-8').strip()
				data['location'] = details[1].text.encode('utf-8').strip()
				data['company'] = details[2].text.encode('utf-8').strip()
				data['short_description'] = tr.find_next_sibling('tr').td.div.div.text.encode('utf-8').strip().replace('\r', '').replace('\n', '').replace('\t', '')
				#~ print data				
				f.write("{}\n".format(json.dumps(data, sort_keys=True, indent=4)))
			f.close

if __name__ == '__main__':
	keywords = ['python']

	scraper = Scraper()
	scraper.search(keywords)

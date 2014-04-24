import cProfile
import json
import requests
from bs4 import BeautifulSoup

class Scraper(object):
	def __init__(self):
		pass
	
	def search(self, keywords=['java']):
		page = pages = 1
		
		for keyword in keywords:
			
			payload = {'q':keyword, 'searchType':'jobs', 'page':page}
			r = requests.get('http://cebu.mynimo.com/jobs/search/?', params=payload)
			pages = self.__get_pages(r)
			
			for page in xrange(1, pages+1):
				#~ print '>>>', keyword, page
				payload = {'q':keyword, 'searchType':'jobs', 'page':page}
				r = requests.get('http://cebu.mynimo.com/jobs/search/?', params=payload)
				if r.status_code == requests.codes.ok:
					self.__extract_data(r, keyword)
				else:
					raise Exception('There seems to be a problem connecting to the site.')
	
	def __get_pages(self, r):
		soup = BeautifulSoup(r.text, from_encoding='utf-8')
		paginator = soup.find('ul', {'class':'paginator'})
		try:
			for child in paginator.findChildren('li'):
				if child.text.isdigit(): pages = child.text
		except:
			pages = 1
		return int(pages)
	
	def __extract_data(self, r, keyword):
		soup = BeautifulSoup(r.text, from_encoding='utf-8')
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
				data['short_description'] = tr.find_next_sibling('tr').td.div.div.text.encode('utf-8').strip()
				#~ print data				
				f.write("{}\n".format(json.dumps(data, sort_keys=True, indent=4)))
			f.close

if __name__ == '__main__':
	keywords = ['python']
	
	scraper = Scraper()
	scraper.search(keywords)

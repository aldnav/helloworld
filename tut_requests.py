import requests
from bs4 import BeautifulSoup
#~ soup = BeautifulSoup(html_doc)
#~ url = 'http://cebu.mynimo.com/jobs/search/?q={0}&searchType=jobs&page=1'.format(keyword)

def search_by_keyword(keyword='java'):
	url = 'http://www.pythonforbeginners.com'
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data)
	for link in soup.find_all('a'):
		print link.get('href')
	#~ r = requests.post('http://cebu.mynimo.com/jobs/search/?q={0}&searchType=jobs&page=1'.format(keyword))
	#~ return r

result = search_by_keyword('python')
print result

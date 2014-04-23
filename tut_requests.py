import requests
from bs4 import BeautifulSoup

def search_by_keyword(keyword='java'):
	url = 'http://www.pythonforbeginners.com'
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data)
	for link in soup.find_all('a'):
		print link.get('href')
	r = requests.post('http://cebu.mynimo.com/jobs/search/?q={0}&searchType=jobs&page=1'.format(keyword))
	return r

#~ result = search_by_keyword('python')
#~ print result

start_url = requests.get('http://cebu.mynimo.com/jobs/search/?q=java&searchType=jobs&page=1')
soup = BeautifulSoup(start_url.content)
results = soup.find_all('a', {'class':'jobTitleLink'})
jobtitles = []
for result in results:
	jobtitles.append(result.getText())
results = soup.find_all('td', {'class':'search_highlight'})
locations = []
for result in results:
	locations.append(result.getText())
print locations

import sys
import re
import urllib2
from BeautifulSoup import BeautifulSoup, SoupStrainer
from urlparse import urljoin
from urlparse import urlparse

def get_url_content(site_url):
	rt=""
	try:
		request = urllib2.Request(site_url)
		f=urllib2.urlopen(request)
		content=f.read()
		f.close()
	except urllib2.HTTPError, error:
		content=str(error.read())
	return content

 
def get_all_links(site_url):
	new_string=""
	for link in BeautifulSoup(get_url_content(site_url), parseOnlyThese=SoupStrainer('a')):
		if link.has_key('href'):
			if link['href'].startswith("javascript:"):
				continue
			if link['href'].startswith("http"):
				new_string = new_string + str(link['href']) + "\n"
			else:
				new_string = new_string + str(urljoin(site_url),link['href'])) + "\n"
	return new_string


if __name__ == "__main__":
	input_url=sys.argv[1]
	opt_file=sys.argv[2]
	outdata=open(opt_file,'w+')
	outdata.write(get_all_links(input_url))
	outdata.close()

				
 

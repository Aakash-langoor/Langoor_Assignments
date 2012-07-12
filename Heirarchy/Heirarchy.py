import sys
import re
import os
import urllib2
from urlparse import urljoin
from urlparse import urlparse
from BeautifulSoup import BeautifulSoup, SoupStrainer

def get_url_content(site_url):
	try:
		request = urllib2.Request(site_url)
		f=urllib2.urlopen(request)
		content=f.read()
		f.close()
	except urllib2.HTTPError, error:
		content=str(error.read())
	return content


def get_all_links(site_url):
	parsed = urlparse(site_url)
	for link in BeautifulSoup(get_url_content(site_url), parseOnlyThese=SoupStrainer('a')):
		if link.has_key('href'):
			if link['href'].startswith("http"):
				if link['href'].startswith("http://"+parsed.netloc):
					newparse=urlparse(link['href'])
					if "." in os.path.basename(link['href']):
						os.makedirs(parsed.netloc+"/"+newparse.path)
						a=open(parsed.netloc+"/"+newparse.path+"/"+os.path.basename(link['href']), 'w')
						a.write(get_url_content(link['href']))
					else:
						os.makedirs(parsed.netloc+"/"+newparse.path)
						b=open(parsed.netloc+"/"+newparse.path+"/"+"index.html", 'w')
						b.write(get_url_content(link['href']))	  
			else:
				new_url=urljoin("http://"+parsed.netloc,link['href'])	  
				pparse=urlparse(new_url)
				if "." in os.path.basename(new_url):
					os.makedirs(parsed.netloc+"/"+pparse.path)
					c=open(parsed.netloc+"/"+newparse.path+"/"+os.path.basename(new_url), 'w')
					c.write(get_url_content(new_url))	  
				else:
					os.makedirs(parsed.netloc+"/"+pparse.path)
					d=open(parsed.netloc+"/"+pparse.path+"/"+"index.html", 'w')
					d.write(get_url_content(new_url))

if __name__ == "__main__":
	input_url=sys.argv[1]
	get_all_links(input_url)

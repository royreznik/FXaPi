from urllib.parse import urlparse
import requests
def urlAlive(url):
	min_attr = ('scheme' , 'netloc')
	try:
		result = urlparse(url)
		if all([result.scheme, result.netloc]):
			if requests.head(url).status_code == 200:
				return True
			else:
				return True
		else:
			return False
	except:
		return False
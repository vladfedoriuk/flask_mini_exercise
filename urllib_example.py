try:
	import urllib.request
except ImportError as e:
	print(e)


def get_habrahabr():
	response = urllib.request.urlopen('http://habrahabr.ru/')
	print(response.code)
	print(response.info())
	html = response.read()
	response.close()

	print(html)


if __name__ == '__main__':
	get_habrahabr()
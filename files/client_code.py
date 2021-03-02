import requests

def send(url, **data):
	try:
		response = requests.post(
			url=url,
			data=data,
			)
		response.raise_for_status()
		print(response.text)
	except requests.HTTPError as he:
		print(f'http error: {he}')
	except Exception as e:
		print(f'Exception: {e}')

if __name__=='__main__':
	#send('http://127.0.0.1:5000', name='vlad', email='fed@ukr.net', job='IT', date=5)
	#send('http://127.0.0.1:5000/locales', locale='fr')
	send('http://127.0.0.1:5000/form/user', email="vlad@ukr.net", password="123456", confirmation="12356")code
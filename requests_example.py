import requests
import json


def get_habrahabr():
	r = requests.get('http://habrahabr.ru')
	print(r.status_code)
	print(r.headers)
	print(r.content)


def write(txt, mode='w'):
	with open('data.txt', mode=mode) as f:
		f.write(txt)

def find_pet_by_tag(tag):
	params = {'tags': tag}
	headers = {
		#'Accept': 'application/xml'
		'Accept': 'application/json'
	}
	url = 'http://petstore.swagger.io/v2/pet/findByTags'
	req = requests.get(url=url, params=params, headers=headers)
	print(req.status_code, req.headers)
	s = str(req.content, encoding='utf-8')
	obj  = json.loads(s)
	write(json.dumps(s, indent=4, sort_keys=True))

if __name__ == '__main__':
	# get_habrahabr()
	find_pet_by_tag('string')

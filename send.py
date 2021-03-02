import requests
import sys

def send(url, data):
	try:
		response = requests.post(
			headers={
				"content-type": "application/json"
			},
			url=url,
			json=data,
			)

		response.raise_for_status()
		print(response.text)
	except requests.HTTPError as he:
		print(f'HTTPEsrror: {he}')
	except Exception as e:
		print(f'Exception: {e}')

if __name__=='__main__':
	#send('http://127.0.0.1:5000', name='vlad', email='fed@ukr.net', job='IT', date=5)
	#send('http://127.0.0.1:5000/locales', locale='fr')
	# send('http://127.0.0.1:5000/form/user', email="vlad@ukr.net", password="123456", confirmation="12356")
	"""print(requests.get(url='http://127.0.0.1:5000/').text)
	for num in range(1, 11):
		print(num)
		send('http://127.0.0.1:5000/guess', guess = num """
	#send('http://127.0.0.1:5000/', observation_date ="2021-12-20", people_available=47)
	"""if len(sys.argv)==2 and sys.argv[1] == '--usage':
		print(f"Usage pattern:  {sys.argv[0]}  url=some_url field1=value1 field2=value2 ... ")
	else:
		try:
			data = {arg[:arg.index('=')] : arg[arg.index('=')+1:] for arg in sys.argv[1:]}
		except ValueError as ve:
			print(f"ValueError: {ve},\n\t correct usage: url=some_url field1=value1 field2=value2 ... ")
		url = data.get('url')
		try:
			data.pop('url')
		except KeyError as ke:
			print(f"KeyError: {ke}, url has not been specified")
		send(url, **data) """

	# send(url='http://127.0.0.1:5000/doctors/', id=105, hospital_id=2, speciality='Therapist', salary=10500.7, experience=7, doctor_name='Zoe', joining_date='2015-05-06 23:23:23')
	# send(url='http://127.0.0.1:5000/doctors/', id=104, hospital_id=3, speciality='Surgeon', salary=30400.5, experience=2, doctor_name='Mark')
	# send(url='http://127.0.0.1:5000/doctors/', id=103, hospital_id=2, speciality='Oncologist', salary=20500.5, experience=4, doctor_name='John')
	send(url='http://127.0.0.1:8000/api/v1/routes/', 
			data={
			"waypoints": "[[29.920846,50.06863],[29.817856,50.044579]]",
  			"user": 2,
  			"route_type": 1,
  			"passengers": 0,
  			"active": True,
  			"sun": True,
  			"mon": True,
  			"tue": True,
  			"wed": True,
  			"thu": True,
  			"fri": True,
  			"sat": True,
  			"sun_start": "string",
  			"mon_start": "string",
  			"tue_start": "string",
  			"wed_start": "string",
  			"thu_start": "string",
 			"fri_start": "string",
  			"sat_start": "string",
  			"delta": 0,
  			"day_of_month": 0,
  			"price_of_ride": 0,
  			"periodic": True,
  			"description": "string",
  			"waypoints_description": '',
		})
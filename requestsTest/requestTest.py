import requests
import random

url = 'scam.com'

for i in range(1000):

	username = ''
	password = ''

	for i in range(5):
		username += str(random.choice(url.replace("/", '')))
	for i in range(8):
		password += str(random.choice(url.replace("/", '')))


	data = {"login": username,
			"password": password}

	response = requests.post(url, data=data).text

	print(username, "|", password)

	print(response)
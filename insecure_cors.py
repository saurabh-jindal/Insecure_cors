#!/usr/bin/python
import requests

with open('quora_domains.txt','r') as f:
	data = f.readlines()


data = [x.strip() for x in data]
data = ["http://" + str(x) for x in data]


for n in data:
	url = n
	header = {'Origin':'www.bing.com'}
	r = requests.get(url, headers=header)

	print r.status_code
	for k,v in r.headers.items():
		print("%s : %s" % (k,v))
	print("\n")
	print("\n")	
	try:
		print r.headers['Access-Control-Allow-Origin']
		print r.headers['Access-Control-Allow-Credentials']
	except:
		pass






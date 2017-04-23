import requests
import json

username = raw_input("Enter username: ")
t = requests.get('https://keybase.io/_/api/1.0/user/lookup.json?usernames='+username)
data = json.loads(t.text)
if (data['them'] == [None]):
	print "[-] The user doesnt exist on KeyBase"
else:
	bio = data['them'][0]['profile']['bio']
	location = data['them'][0]['profile']['location']
	full_name = data['them'][0]['profile']['full_name']
	print "Full name : " + full_name
	print "Bio : " + bio
	print "Location : " + location
	i = 0
	while True:
		try:
			print data['them'][0]['proofs_summary']['all'][i]['service_url']
			i = i+1
		except:
			break
	print "For more details look: https://keybase.io/"+username

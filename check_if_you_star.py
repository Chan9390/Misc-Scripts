import requests
import simplejson
import time
import os

def star_check(repo):
	try:
		temp_url = "https://api.github.com/user/starred/" + str(repo) + "?access_token=" + str(token)
		r = requests.get(temp_url)
		if r.status_code == 404:
			tmp = "https://api.github.com/repos/" + str(repo) + "?access_token=" + str(token)
			res = requests.get(tmp)
			tmp_js = simplejson.loads(res.content)
			os.system("cls")
			print str(repo)
			print str(tmp_js["description"])
			ch = raw_input("Do you want to add this: ")
			if ch == 'y':
				with open("repos.txt", "a") as myfile:
					myfile.write(str(repo) + "\n")
			print ""
		time.sleep(0.5)
	except:
		pass

def get_stars(target):
	page_count = 1
	url = "https://api.github.com/users/" + str(target) + "/starred?access_token=" + str(token) + "&per_page=100&page="
	while(page_count > 0):
		temp_url = url + str(page_count)
		r=requests.get(temp_url,)
		#print r.content
		js=simplejson.loads(r.content)
		if len(js) == 0:
			cnt = 0
		else:
			for a in range(0, js.__len__()):
				star_check(js[a]["full_name"])
			#print js[0]
			page_count += 1
			time.sleep(1)

if __name__ == '__main__':
	global token
	token = raw_input("Enter access token: ")
	user = raw_input("Enter target: ")
	get_stars(user)
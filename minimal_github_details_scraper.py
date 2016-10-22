from bs4 import BeautifulSoup as bs
import requests

'''
Unchecked conditions:
  * Space in username
  * No internet connection
  * SSL interception (If there is some SSL connection error, it turns out to be an error)
  * Error codes (301, 302, 500, etc)
These conditions may be considered in the future releases
'''

def return_num(a):
	temp = [int(s) for s in str(a).split() if s.isdigit()]
	return temp[0]

if __name__ == '__main__':
	name = raw_input("Enter the name: ")
	url = "https://github.com/" + name
	r = requests.get(url)
	soup = bs(r.content, "lxml")
	hrefs = soup.find_all('a', attrs={'class':'underline-nav-item'})

	repo_soup = hrefs[1]
	star_soup = hrefs[2]
	follower_soup = hrefs[3]
	following_soup = hrefs[4]

	print "Details of the user: "
	print "Repos     : " + str(return_num(repo_soup))
	print "Stars     : " + str(return_num(star_soup))
	print "Followers : " + str(return_num(follower_soup))
	print "Following : " + str(return_num(following_soup))

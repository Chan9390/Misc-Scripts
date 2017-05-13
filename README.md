# Misc-Scripts
Random scripts which helped me to improve my programming skills

#### `check_if_you_star.py`
If I wanted to star all the repos starred by someone, I use this script. It requires *API Access token* for the account from which you want to star. The script gets the starred repos of a person, and if the repo is not starred by you then it shows the description of the starred repos and asks whether to add it to the list. If 'y' is pressed, it adds the fullname of the repo to the file `repos.txt` which can later be automatically starred by another script.

#### `minimal_github_details_scraper.py`
I required the total count of starred repositories of a username on GitHub in order to automate something. I researched a lot and found that there is no direct way to find the number of starred repositories. One possible way was to use the Github API for getting starred repo one per page and count the total number of pages (find more about the indirect solution [here](http://stackoverflow.com/questions/30636798/get-user-total-starred-count-using-github-api-v3)) One major disadvantage of the above mentioned method is, if the target user had >100 one would require API token/keys to send large number of requests (By the way GitHub has a limit to the number of unauthenticated API requests). So ended up making a custom script which will scrape the information (repos, stars, followers, following) directly from the GitHub profile page.

#### `keybase.py`
Analyse keybase users

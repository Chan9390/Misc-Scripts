# Misc-Scripts
Random scripts which helped me to improve my programming skills

#### `minimal_github_details_scraper.py`
I required the total count of starred repositories of a username on GitHub in order to automate something. I researched a lot and found that there is no direct way to find the number of starred repositories. One possible way was to use the Github API for getting starred repo one per page and count the total number of pages (find more about the indirect solution [here](http://stackoverflow.com/questions/30636798/get-user-total-starred-count-using-github-api-v3)) One major disadvantage of the above mentioned method is, if the target user had >100 one would require API token/keys to send large number of requests (By the way GitHub has a limit to the number of unauthenticated API requests). So ended up making a custom script which will scrape the information (repos, stars, followers, following) directly from the GitHub profile page.

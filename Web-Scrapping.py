import requests
from bs4 import BeautifulSoup as bs

GitHubUser = input("Enter the GitHub user: ")
url = 'https://github.com/'+GitHubUser
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profileImage = soup.find('img', {'alt' : 'Avatar'})['src']
print(profileImage)

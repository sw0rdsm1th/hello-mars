import urllib.request
from bs4 import beautifulsoup

#Wanted to read from Hacker News
html = urllib.request.urlopen('https://news.ycombinator.com/').read()
soup = BeautifulSoup(html, 'html.parser')
texts = soup.findAll(text=True)

# Looping through proper tags to print the links for articles, but I got more than I bargained for since I didn't specify the types of a tags

#for a in soup.find_all('a'):
#print(a)

#Just text of the news articles

for td in soup.find_all('td'):
    print(td.get_text())

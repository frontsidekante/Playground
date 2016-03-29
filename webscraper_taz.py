import requests
from bs4 import BeautifulSoup

# send request
url = 'http://www.taz.de'
r = requests.get(url)

# increase readability of response
soup = BeautifulSoup(r.content, 'lxml')
# print soup.prettify()


print '----------- topics, focus'
h2 = soup.find_all('h2')
for link in h2:
        print link.text

print '----------- sexy title'
h3 = soup.find_all('h3')
for link in h3:
    print link.text

print '---------- serious title'
h4 = soup.find_all('h4')
for link in h4:
    print link.text
#TODO: exclude (Die Wahrheit, Die Woche vom x...y)



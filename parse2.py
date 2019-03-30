from bs4 import BeautifulSoup
import requests

page_link = 'http://forex-brokers.pro/sitemap.html'
# fetch the content from url
page_response = requests.get(page_link, timeout=5)
# parse html
page_content = BeautifulSoup(page_response.content, "html.parser")


# prices = page_content.find_all('a')
#
#
# print(prices)
f = open('text2.txt', 'w')
for link in page_content.find_all('a'):
    f.write('http://forex-brokers.pro' + link.get('href')+ '\n')
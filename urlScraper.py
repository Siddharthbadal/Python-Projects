import requests
from bs4 import BeautifulSoup
import pprint
import re 

def scraper():
    baseurl = input("Enter the url you want scrape.. ")
    page = requests.get(baseurl)
    soup = BeautifulSoup(page.text, 'html.parser')

    urlAddress = []
    for link in soup.find_all('a', attrs={'href': re.compile("^http")}):
            pprint.pprint(f"{link.string} ---> {link.get('href')}")
            # urlAddress.append(link.get('href'))

    return urlAddress


scraper()

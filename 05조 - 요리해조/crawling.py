import requests 
import bs4


URL = 'https://www.10000recipe.com/recipe/'

def crawl():
    response = requests.get(URL+'128671')
    soup = bs4.BeautifulSoup(response.text,"html.parser")
    print(soup.find('div',{'class':'ready_ingre3'}).text)

if __name__=='__main__':
    crawl()
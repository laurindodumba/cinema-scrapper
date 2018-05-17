from bs4 import BeautifulSoup
import requests

URL='http://www.gartenshopping.com.br'

def pega_links():
    links = []
    r = requests.get(URL + '/cinema')
    response_text = r.text

    parsed_html = BeautifulSoup(response_text, 'html.parser')
    cinema_text = parsed_html.body.find('div', attrs={'class': 'item-list-content'})

    for link in cinema_text.find_all('a'):
        links.append(link.get('href'))
    
    return links
      

def informacao_do_filme(link):
    r = requests.get(URL + link)
    response_text = r.text

    parsed_html = BeautifulSoup(response_text, 'html.parser')
    return parsed_html


links = pega_links()
for link in links:
    print(informacao_do_filme(link))

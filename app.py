from bs4 import BeautifulSoup
import requests

r = requests.get('http://www.gartenshopping.com.br/cinema')
response_text = r.text

parsed_html = BeautifulSoup(response_text, 'html.parser')
cinema_text = parsed_html.body.find('div', attrs={'class':'cinema-date-filter'})

for link in cinema_text.find_all('a'):
    print(link.get('href'))
import requests
from bs4 import BeautifulSoup

mystocks = ['GME', 'RKT', 'TSLA', 'AMC', 'BB', 'NOK']
stockdata = []

def getData(symbol):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0'}
    url = f'https://finance.yahoo.com/quote/{symbol}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    stock = {
    #These Selectors wont work for multiple stocks but they work for GME
    #price = soup.find('span', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
    #change = soup.find('span', {'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'}).text
    'symbol': symbol,
    'price': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[0].text,
    'change': soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[1].text,
    }
    return stock

for item in mystocks:
    stockdata.append(getData(item))
    print("getting: ", item)

print(stockdata)
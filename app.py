from bs4 import BeautifulSoup
import requests
from time import sleep
import pandas as pd
url = "https://www.century21.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/?ty=0"

response = requests.get(url)
c = response.content
sleep(2)
soup = BeautifulSoup(c,'html.parser')
# print(soup)
all = soup.find("div",{'class':'infinite-container'})
# print(all)
alls = [ i for i in soup.find_all("div",{'class':'infinite-item'}) ]
# print(alls)
d = {}
l = []
for i in alls:
    price = i.find('a',{'class':'listing-price'},text=True)
    if price:
        d['price'] = price.get_text().strip()
    beds= i.find('div',{'class':'property-beds'})
    if beds:
        d['beds'] = beds.get_text().strip()
    bath = i.find('div',{'class':'property-baths'})
    if bath:
        d['bath'] = bath.get_text().strip()

    address = i.find('div',{'class':'property-address'})
    if address:
        d['address'] = address.get_text().strip()

    address_city = i.find('div',{'class':'property-address-city'})
    if address_city:
        d['address_city'] = address_city.get_text().strip()
    l.append(d)

df = pd.DataFrame(l)
print(df.head(3))
df.to_csv('output.csv', mode='a',header=False)
from bs4 import BeautifulSoup
import requests as req
url = 'https://goodlooker.ru/kak-pohudet-za-nedelju.html'
r = req.get(url)
# soup = BeautifulSoup(r.text,'html.parser')
# page = soup.find_all('div',class_='post')
# print (page)
soup = BeautifulSoup(r.text, 'html.parser')
headers = soup.find_all('ol')
Adviсe = []
for h in headers:
    Adviсe.append(h.li.text)
cur = 1
for adv in Adviсe:
    print(f'{cur}. {adv}')
    cur += 1

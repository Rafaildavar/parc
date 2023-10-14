from bs4 import BeautifulSoup
import requests as req
url = 'https://goodlooker.ru/kak-pohudet-za-nedelju.html'
r = req.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
headers = soup.find_all('h3')

Sunday = []
Monday = []
Tuesday = []
Wednesday = []
Thursday = []
Friday = []
Saturday = []
cur = 0
cycle = 0
for header in headers:
    if cycle == 0 :
        Sunday.append(header.text)
        cur +=1
    if cycle == 1 :
        Monday.append(header.text)
        cur +=1
    if cycle == 2 :
        Tuesday.append(header.text)
        cur +=1
    if cycle == 3 :
        Wednesday.append(header.text)
        cur +=1
    if cycle == 4 :
        Thursday.append(header.text)
        cur +=1
    if cycle == 5 :
        Friday.append(header.text)
        cur +=1
    if cycle == 6 :
        Saturday.append(header.text)
        cur +=1

    if cur == 10:
        cur = 0
        cycle += 1
print('PLAN TRAIN IN Tuesday:')

for day in Monday:
    print(day)
for day in Thursday:
    print(day)
for day in Tuesday:
    print(day)
for day in Wednesday:
    print(day)
for day in Friday:
    print(day)
for day in Sunday:
    print(day)
for day in Saturday:
    print(day)








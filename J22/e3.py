import requests
from bs4 import BeautifulSoup
import json

url='https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

try:
    response=requests.get(url)
    if response.status_code==200:
        content=response.content
        soup=BeautifulSoup(content, 'html.parser')

        table=soup.body.find('table', class_='wikitable sortable sticky-header')
        data=[]
        
        for tr in table.find_all('tr'):

            row={}
            row['no']=tr.th.get_text()
            cells=tr.find_all('td')
            if len(cells)==0:
                continue

            row['portrait']=cells[0].a['href']
            row['name']=cells[1].b.get_text(strip=True)
            row['term']=cells[2].get_text(strip=True)
            row['party']=cells[4].get_text(strip=True).encode('ascii', 'ignore').decode('ascii')
            row['election']=cells[5].get_text(strip=True)
            row['vice_president']=cells[6].get_text(strip=True)
            data.append(row)

        with open('wiki_us_presidents.json', '+w') as file:
            file.write(json.dumps(data, indent=4))
    else:
        print('The url we are trying to reach is not avaibble')
except Exception as e:
    print('An error occured: ', e)
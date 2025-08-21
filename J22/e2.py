import requests
from bs4 import BeautifulSoup
import json
import sys

url='https://archive.ics.uci.edu/datasets'

try:
    response=requests.get(url)
    if response.status_code==200:
        content=response.content
        soup=BeautifulSoup(content, 'html.parser')

        items=soup.body.main.find_all('div', class_='relative col-span-8 sm:col-span-7')
        data=[]
        
        for item in items:
            row={}
            row['title']=item.h2.a.get_text()
            row['description']=item.p.get_text(strip=True)
            details=item.find('div', class_='my-2 hidden gap-4 md:grid grid-cols-12').find_all('span')
            row['task']=details[0].get_text(strip=True)
            row['type']=details[1].get_text(strip=True)
            row['instances']=details[2].get_text(strip=True)
            row['features']=details[3].get_text(strip=True)
            data.append(row)

        with open('uci_dataset.json', '+w') as file:
            file.write(json.dumps(data, indent=4))
    else:
        print('The url we are trying to reach is not avaibble')
except Exception as e:
    print('An error occured: ', e)
import requests
from bs4 import BeautifulSoup
import json

url='https://www.bu.edu/president/boston-university-facts-stats'

try:
    response=requests.get(url)
    if response.status_code==200:
        content=response.content
        soup=BeautifulSoup(content, 'html.parser')
        data={}
        data["title"]=soup.body.find('h3', class_='bu-banner-title font-size-1').get_text(strip=True)
        data["description"]=soup.body.find('h4', class_='bu-banner-subtitle font-size-3').get_text(strip=True)
        facts=[]

        container=soup.body.main.find('article', id='post-23')

        stat_list=container.find('div', class_='bu-stat-list bu-stat-count-3')
        data_titles=container.find_all('h4', class_='stat-group-title')
        title0=data_titles[0].get_text()
        data[title0]={}
        for article in stat_list.find_all('article'):
            data[title0][article.find('h3', class_='bu-stat-title').get_text(strip=True)]=article.find('div', class_='bu-stat-element').get_text(strip=True)

        title1=data_titles[1].get_text()
        stat_list=container.find('div', class_='facts-stats-content')
        sections=stat_list.find_all('section')
        data[title1]={}
        for li in sections[0].find_all('li'):
            data[title1][li.find_all('span')[0].get_text(strip=True)]=li.find_all('span')[1].get_text(strip=True)

        title2=data_titles[2].get_text()
        stat_list=container.find('div', class_='bu-stat-list bu-stat-count-5')
        data[title2]={}
        for article in stat_list.find_all('article'):
            data[title2][article.find('h3', class_='bu-stat-title').get_text(strip=True)]=article.find('div', class_='bu-stat-element').get_text(strip=True)
        
        title3=data_titles[3].get_text()
        data[title3]={}
        for li in sections[1].find_all('li'):
            data[title3][li.find_all('span')[0].get_text(strip=True)]=li.find_all('span')[1].get_text(strip=True)

        with open('boston_university_facts.json', '+w') as file:
            file.write(json.dumps(data, indent=4))

    else:
        print('The url we are trying to reach is not avaibble')
except Exception as e:
    print('An error occured: ', e)
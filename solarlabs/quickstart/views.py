from django.shortcuts import render


import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bs4 import BeautifulSoup

# Create your views here.
@api_view(['GET'])
def get_natDetails(request,country_name):
    flag_link, capital, l_city, off_lang, area, population, gdp = '', [], [], [], 0, 0, ''
    url = "https://en.wikipedia.org/wiki/"+country_name
    # HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36','Accept-Language':'en-US, en;q=0.5'})

    

    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    table = soup.find("table",attrs={"class":"infobox ib-country vcard"})
    
    # fetch website
    flag_link = table.find("a", attrs={'class': "image"}).find("img")
    flag_link = "https://" + flag_link.get('src')
    
    pairs = table.find_all('tr')
    for pair in pairs:
        if pair.find('th'):
            heading = pair.find('th')
            detail = pair.find('td')
            print(heading.text)
            if heading.text == 'Capitaland largest city':
                capital = [i.get('title') for i in detail.find_all('a') if i.get('title') is not None]
                l_city = capital
                if len(capital) == 1:
                    capital = capital[0]
                    l_city = capital
            if heading.text == 'Capital':
                capital = [i.get('title') for i in detail.find_all('a') if i.get('title') is not None]
                if len(capital) == 1:
                    capital = capital[0]
            if heading.text == 'Largest city':
                l_city = [i.text for i in detail.find_all('a') if i.get('title') is not None]
                if len(capital) == 1:
                    l_city = l_city[0]
            if 'Official' in heading.text and 'languages' in heading.text:
                off_lang = [i.text for i in detail.find_all('a') if i.get('title') is not None]
                if len(off_lang) == 1:
                    off_lang = off_lang[0]
    for c in range(len(pairs)):
        th_data=pairs[c].find('th')
        if(th_data!=None and th_data.find('a')!=None and th_data.find('a').get_text()=="Area "):
            area= pairs[c+1].find('td').get_text().split('[')[0].split('(')[0]

        if(th_data!=None and th_data.find('a')!=None and th_data.find('a').get_text()=="Population"):
            population= pairs[c+1].find('td').get_text().split('[')[0].split('(')[0]

        if(th_data!=None and th_data.find('a')!=None and th_data.find('a').get_text()=="GDP" and th_data.find('span').get_text()=="(nominal)"):
            gdp= pairs[c+1].find('td').get_text().split('[')[0]

    return Response({"flag_link":flag_link,"capital":capital,"largest_city":l_city,"offical_languages":off_lang,"area_total":area,"Population":population,"GDP_nominal":gdp})

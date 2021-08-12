import pandas as pd
from bs4 import BeautifulSoup
import requests as req
import urllib.request
import time
import numpy as np
from datetime import datetime

prices = []
spaces = []
municipalities = []
blocks = []
streets = []
dates = []
links = []
pricePerSpaces = []
rooms = []
floors = []
advertisers = []
pageUrl = 'https://www.halooglasi.com/nekretnine/prodaja-stanova/beograd?page='
domain = 'https://www.halooglasi.com'





def extractData(flats,prices = [],spaces = [],municipalities = [],blocks = [],streets = [],dates = [],links = [],domain = ''):
    for flat in flats:

        price  = ''
        space = ''
        municipality = ''
        block = ''
        street = ''
        date = ''
        room = ''
        floor = ''
        oglasivac = ''
        pricePerSpace = ''
        link  = domain

        price = flat.find('i').text[:-2].replace(',','.')
        
        space = flat.findAll('div', attrs={'class':'value-wrapper'})[0].text[:-13].replace(',','.')
        
        room = flat.findAll('div', attrs={'class':'value-wrapper'})
        
        #fixing room nmber
        if len(room) > 1:
            room = room[1].text[:-10].replace(',','.')
       
        floor = flat.findAll('div', attrs={'class':'value-wrapper'})
        
        #fixing floor number
        if len(floor) > 2:
            floor = floor[2].text[:-10].replace(',','.')
        else: floor = 'N/A'
        
        pricePerSpace = flat.findAll('div', attrs={'class':'price-by-surface'})[0].text[:-5].replace(',','.')

        oglasivac = flat.findAll('span', attrs={'data-field-name':'oglasivac_nekretnine_s'})
        
        if len(oglasivac) > 0:
            oglasivac= oglasivac[0].text[:-1]

        addressDetail = flat.find('ul', attrs={'class': 'subtitle-places'}).findAll('li')

        if len(addressDetail) >= 2:
            municipality = addressDetail[1].text[:-1]

        if len(addressDetail) >= 3:
            block = addressDetail[2].text[:-1]

        if len(addressDetail) >= 4:
            street = addressDetail[3].text[:-1]

        date = flat.find('span', attrs ={'class':'publish-date'}).text
        
        link = domain + flat.find('h3', attrs={'class':'product-title'}).find('a')['href']

        prices.append(price)
        spaces.append(space)
        municipalities.append(municipality)
        blocks.append(block)
        streets.append(street)
        dates.append(date)
        links.append(link)
        pricePerSpaces.append(pricePerSpace)
        rooms.append(room)
        floors.append(floor)
        advertisers.append(oglasivac)
    
    return {'prices':prices,
            'spaces':spaces,
            'municipalities':municipalities,
            'blocks':blocks,
            'streets':streets,
            'dates':dates,
            'links':links,
            'pricePerSpaces':pricePerSpaces,
            'rooms':rooms,
            'floors':floors,
            'advertisers':advertisers}



for page in range(1,887):
    try:
        
        serachUrl = pageUrl + str(page)
        print(page)
        
        response = req.get(serachUrl)

        soup = BeautifulSoup(response.content,"html.parser")

        premiumFlats = soup.findAll('div',attrs={'class':'product-item product-list-item Premium real-estates my-product-placeholder'})
        topFlats = soup.findAll('div',attrs={'class':'product-item product-list-item Top real-estates my-product-placeholder'})
        standardFlats = soup.findAll('div',attrs={'class':'product-item product-list-item Standard real-estates my-product-placeholder'})
        distingushedFlats = soup.findAll('div', attrs={'class': 'product-item product-list-item Distinguished real-estates my-product-placeholder'})
        
        extractData(premiumFlats,prices,spaces,municipalities,blocks,streets,dates,links,domain)
        extractData(topFlats,prices,spaces,municipalities,blocks,streets,dates,links,domain)
        extractData(standardFlats,prices,spaces,municipalities,blocks,streets,dates,links,domain)
        extractData(distingushedFlats,prices,spaces,municipalities,blocks,streets,dates,links,domain)
        
        time.sleep(0.3)
    
    except Exception as e:
        print(str(e))

#getSnapskotDate
snapshotDate = datetime.today().strftime('%d.%m.%Y')
snapshotDate = [snapshotDate]*len(prices)
yyymmdd = datetime.today().strftime('%Y%m%d')
links = list(map(lambda x:yyymmdd+ 'id'+ x[37:len(x)],links))

dataFrame = pd.DataFrame({'Price':prices,'Space':spaces,'PricePerSpace':pricePerSpaces,'Rooms':rooms,'Floors':floors,'Ogasivac':advertisers,'Municipality':municipalities,'Area':blocks,'Address':streets,'LastChanged':dates,'Link':links, 'snapshotDate':snapshotDate})


dataFrame.to_csv('AdsBeograd'+yyymmdd+'.csv',encoding='utf-16',sep='\t', index=False)

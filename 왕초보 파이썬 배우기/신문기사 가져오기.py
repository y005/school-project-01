# -*- coding: utf-8 -*-
"""
Created on Thu May 31 14:33:05 2018

@author: SM-PC
"""

import bs4
import lxml
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


def getTheNews(xml_news_url):
    
    client = urlopen(xml_news_url)
    xml_page = client.read()
    client.close()
    
    soup_page = soup(xml_page,'xml')
    news_list = soup_page.findAll('item')
 
    for news in news_list:
        print(news.title.text)
        print(news.link.text)
        print(news.pubDate.text)
        print('\n\n')
        
        
        
        
        
mynews_url = 'https://news.google.com/news/rss/?ned=us&gl=US&hl=en'
   
getTheNews(mynews_url)     
        
        
    
    
    
    
    
    
    
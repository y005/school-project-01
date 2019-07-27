
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import the modules
import tkinter as tk
import tkinter.scrolledtext as tkst

import bs4
import lxml
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

#create a tkinter object
window = tk.Tk() #window or root

#give the window a name
window.title('fight')

#give the window a size
window.geometry('800x300')

#create a frame in the window, set the parent and the bg color
frame1 = tk.Frame(master = window,bg = '#808000')

#add the frame to the window                  
frame1.pack(fill ='both',expand = 'yes')    

#create a scrolledtext box
editArea = tkst.ScrolledText(master = frame1 , wrap = tk.WORD, width = 20, height = 10 )              

#add the scrolledtext box to the frame
editArea.pack(padx = 10,pady =10, fill = tk.BOTH , expand = True) 

#create function for gathering the news
def getTheNews(xml_news_url):
    
    theNews = ' '
    client = urlopen(xml_news_url)
    xml_page = client.read()
    client.close()
    
    soup_page = soup(xml_page,'xml')
    news_list = soup_page.findAll('item')
 
    for news in news_list:
        #add the news to scrollable text box 
        editArea.insert(tk.INSERT,news.title.text)
        editArea.insert(tk.INSERT, '\n\n')
        editArea.insert(tk.INSERT,news.link.text)
        editArea.insert(tk.INSERT,news.pubDate.text)
        editArea.insert(tk.INSERT, '\n\n')
        
mynews_url = 'https://news.google.com/news/rss/?ned=us&gl=US&hl=en'
getTheNews(mynews_url)     
        






#run the windowloop-nothing happens without this
window.mainloop()
















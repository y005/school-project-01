import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkst
import bs4
import lxml
import random
import smtplib
from tkinter import TOP
from tkinter import BOTTOM
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from tkinter.colorchooser import askcolor
from tkinter import HORIZONTAL
from tkinter import ROUND
from tkinter import RAISED
from tkinter import SUNKEN
from tkinter import TRUE


window = tk.Tk()
window.title('MOON')
window.geometry('600x480')

def NewsToday():
    window1 = tk.Tk()
    window1.title('News Today')
    window1.geometry('600x360')


    frame1 = tk.Frame(master = window1,bg = 'pink')
    frame1.pack(fill ='both',expand = 'yes')    
    editArea = tkst.ScrolledText(master = frame1 , wrap = tk.WORD, width = 20, height = 10 )              
    editArea.pack(padx = 10,pady =10, fill = tk.BOTH , expand = True) 

    def getTheNews(xml_news_url):
    
        theNews = ' '
        client = urlopen(xml_news_url)
        xml_page = client.read()
        client.close()
    
        soup_page = soup(xml_page,'xml')
        news_list = soup_page.findAll('item')
 
        for news in news_list:
            editArea.insert(tk.INSERT,news.title.text)
            editArea.insert(tk.INSERT, '\n\n')
            editArea.insert(tk.INSERT,news.link.text)
            editArea.insert(tk.INSERT,news.pubDate.text)
            editArea.insert(tk.INSERT, '\n\n')
        
    mynews_url = 'https://news.google.com/news/rss/?ned=us&gl=US&hl=en'
    #'https://newssearch.naver.com/search.naver?where=rss&query=주요뉴스'
    getTheNews(mynews_url)     
    window1.mainloop()
    
#색 변하는 것과 펜의 감촉 오류    
def Drawing():
    class paint(object):
    
        DEFAULT_PEN_SIZE = 5.0
        DEFAULT_COLOR = 'black'
    
        def __init__(self):
      
           self.root = tk.Tk()
           self.root.title ('Painting :D')
      
           self.pen_button = tk.Button(self.root, text = 'pen',command = self.use_pen)
           self.pen_button.grid(row = 0 , column = 0)  
        
           self.brush_button = tk.Button(self.root, text = 'brush',command =self.use_brush)
           self.brush_button.grid(row = 0, column = 1) 
      
           self.color_button = tk.Button(self.root, text ='color',command =self.choose_color)
           self.color_button.grid(row = 0, column = 2)  

           self.eraser_button = tk.Button(self.root, text ='eraser', command = self.use_eraser)
           self.eraser_button.grid(row = 0, column = 3)

           self.choose_size_button = tk.Scale(self.root, from_ = 10, to_ = 100, orient = HORIZONTAL)
           self.choose_size_button.grid(row = 0, column = 4)    
   
           self.c = tk.Canvas(self.root, bg = 'white', width = 600, height = 600)
           self.c.grid(row = 1, columnspan = 5)
      
           self.setup()
           self.root.mainloop()
   
        def setup(self):
        
            self.old_x = None
            self.old_y = None
            self.line_width = self.choose_size_button.get()
            self.color = self.DEFAULT_COLOR
            self.eraser_on = False
            self.active_button = self.pen_button
            self.c.bind('<B1-Motion>', self.paint)
            self.c.bind('<ButtonRelease -1>', self.reset)
      
        def use_pen(self):
            self.activate_button(self.pen_button)
    
    
        def use_brush(self):
            self.activate_button(self.brush_button)
        
        def choose_color(self):
            #self.eraser_on = False
            self.color = askcolor(color = self.color) [1]
        
        def use_eraser(self):
            self.activate_button(self.eraser_button, eraser_mode = True)
     
        def activate_button(self, some_button, eraser_mode = False):
            self.activate_button.config(relief = RAISED)
            some_button.config(relief = SUNKEN)
            self.active_button = some_button
            self.eraser_on = eraser_mode
    
        def paint(self,event):
            self.line_width = self.choose_size_button.get()
            paint_color = 'white' if self.eraser_on else self.color
            if self.old_x and self.old_y:
                self.c.create_line(self.old_x, self.old_y, event.x, event.y,width = self.line_width, fill = paint_color, capstyle = ROUND, smooth = TRUE, splinesteps = 36)
            self.old_x = event.x
            self.old_y = event.y
        
        def reset(self,event):
            self.old_x, self.old_y = None, None
         
    if __name__ == '__main__':
         paint()

def Magic8Ball():
 
    window3 = tk.Tk()
    window3.title('WELCOME')
    window3.geometry('280x100') 
    
    #topframe1 = tk.Frame(window3)
    #topframe1.pack(side = TOP)
    #bottomframe1 = tk.Frame(window3)
    #bottomframe1.pack(side = BOTTOM)
 
    def greetme():
        newtext = 'hello ' + txt.get() + ' I sense a mystery in your heart!'
        lbl.configure(text = newtext)
        newbuttontext = 'True'
        btn.configure(text = newbuttontext,command = askquestion)
        txt.delete(first = 0, last =35)

    def askquestion():
        newtext = 'What is your question?'
        lbl.configure(text = newtext)
        newbuttontext = 'ASK'
        btn.configure(text = newbuttontext,command = getfortune)

    def getfortune():
        newtext = 'AH '+txt.get()+ ' is a good question'
        lbl.configure(text = newtext)
        newbuttontext = 'Yes'
        btn.configure(text = newbuttontext,command = fortuneresult)  
        txt.delete(first = 0, last =35)

    def fortuneresult():
        myrandom = random.randint(0,3)
        if myrandom == 0:
            answer = "Yes, definately! do you need more question?"
        elif myrandom == 1:
            answer = "No way~~~~! Go suck a lemon! do you need more question?"
        else:
            answer = "Ask me later. the sprits are busy. do you need more question?"
        lbl.configure(text = answer)    
        newbuttontext = 'Yes' 
        btn.configure(text = newbuttontext,command = askquestion)
        txt.delete(first = 0, last = 35)     

    lbl = tk.Label(window3,text = 
               'What Is Your Name?'
               ,font = ('Ariel Bold', 12),wraplength = 300)
    lbl.pack()
   
    #image2 = tk.PhotoImage(file = "8-ball.png")
    #imagelabel2 = tk.Label(bottomframe1, image = image2)
    #imagelabel2.pack()

    txt = tk.Entry(window3, width = 35)
    txt.focus()
    txt.pack()
    
    btn = tk.Button(window3, text = 'yes!',command = greetme)
    btn.pack()
    
  
def SendMail():
    window4 = tk.Tk()
    window4.title('Send Mail')
    window4.geometry('600x200')
    mail =[]
    
    def q1():
        mail.append(txt.get())
        lbl.configure(text = 'What Is Your GMAIL PASSWORD?')
        btn.configure(text = 'Okay!', command = q2)
        
    def q2():
        mail.append(txt.get())
        lbl.configure(text = 'What do you want to send?')
        btn.configure(text = 'Okay!', command = send_mail)
            
    def send_mail():
        mail.append(txt.get())
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.ehlo()
        username = mail[0] 
        password = mail[1]
        s.login(username, password)
        replyto = 'send id'
        sendto = ['y005@naver.com']
        sendtoShow = 'y005@naver.com'
        subject = 'email from python class'
        content = mail[2]
        mailtext = 'From: ' + replyto + '\nTo: '+ sendtoShow + '\n'
        mailtext = mailtext + 'Subject: ' + subject + '\n'+ content
        s.sendmail(replyto, sendto, mailtext)
        rslt = s.quit()
        lbl.configure(text = 'Send Mail Results = ' + str(rslt[1]))
        btn.configure(text = 'Okay!')
        
    lbl = tk.Label(window4,text = 
               'What Is Your GMAIL ID?'
               ,font = ('Ariel Bold', 12),wraplength = 300)
    lbl.pack()
    
    txt = tk.Entry(window4, width = 35)
    txt.focus()
    txt.pack()
    
    btn = tk.Button(window4, text = 'Okay!', command = q1)
    btn.pack()
    
    window4.mainloop()

topframe = tk.Frame(window)
topframe.pack(side = TOP)
bottomframe = tk.Frame(window)
bottomframe.pack(side = BOTTOM)

label = tk.Label(topframe, text = 'Hello:D How Can I Help you?', font = ('Arial Bold',30 ))
button1 = tk.Button(bottomframe, text = 'News Today' , command = NewsToday)
button2 = tk.Button(bottomframe, text = 'Drawing' , command = Drawing)
button3 = tk.Button(bottomframe, text = 'Magic 8 Ball' , command = Magic8Ball)
button4 = tk.Button(bottomframe, text = 'Send Mail' , command = SendMail)

label.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()

image1 = tk.PhotoImage(file = "cat1.png")
imagelabel = tk.Label(topframe, image = image1)
imagelabel.pack()

window.mainloop()


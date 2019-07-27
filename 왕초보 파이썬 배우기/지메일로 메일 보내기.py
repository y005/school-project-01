# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
import smtplib


window = tk.Tk()

#start talking to the smtp server for the gmail

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.ehlo()

#log in to the gmail account 
username = '아이디'
password = '비번'
s.login(username, password)

#create the email objects
replyto = '보낸 아이디'
sendto = ['보낼려는 아이디들']
sendtoShow = '보내는 아이디 중 하나'

subject = 'email from python class'
content = '내용\n내용 '

mailtext = 'From: ' + replyto + '\nTo: '+ sendtoShow + '\n'
mailtext = mailtext + 'Subject: ' + subject + '\n'+ 'content'

#send the mail
s.sendmail(replyto, sendto, mailtext)

#close the connection 
rslt = s.quit()

#print the result(fslt)
print('Send Mail Results = ' + str(rslt[1]))

window.mainloop()










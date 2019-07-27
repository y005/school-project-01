import easygui
import random

com = 0
user = 0
game = 1

while True:

    if com == 3 or user == 3:
       if com == 3:
          easygui.msgbox('컴퓨터 '+str(com)+' : '+str(user)+' 사용자\n컴퓨터가 우승했습니다')
          
       else:
          easygui.msgbox('컴퓨터 '+str(com)+' : '+str(user)+' 사용자\n당신이 우승했습니다')

       break

    comn = random.randint(1,3)
    usern = easygui.buttonbox(str(game)+'번째 판\n가위 바위 보 중 하나를 선택하세요: ',choices = ['가위','바위','보'])
     

    # 가위 = 1 바위 = 2 보 = 3

    
    if comn == 1 and usern == '가위':
        easygui.msgbox('모두 가위를 냈습니다. 비겼습니다.\n 컴퓨터 '+str(com)+' : '+str(user)+' 사용자')
        continue
    elif comn == 2 and usern == '바위':
        easygui.msgbox('모두 바위를 냈습니다. 비겼습니다.\n 컴퓨터 '+str(com)+' : '+str(user)+' 사용자')
        continue  
    elif comn == 3 and usern == '보':
        easygui.msgbox('모두 보를 냈습니다. 비겼습니다.\n 컴퓨터 '+str(com)+' : '+str(user)+' 사용자')
        continue
    else:

       if comn == 1 and usern == '바위':

         user += 1
         easygui.msgbox('컴퓨터는 가위를 냈습니다. 당신이 이겼습니다.\n 컴퓨터 '+str(com)+' : '+str(user)+' 사용자')
  
       elif comn == 1 and usern == '보':

         com += 1
         easygui.msgbox('컴퓨터는 가위를 냈습니다. 컴퓨터가 이겼습니다.\n 컴퓨터 '+str(com)+' : '+str(user)+' 사용자')
         
       elif comn == 2 and usern == '가위':

         com += 1
         easygui.msgbox('컴퓨터는 바위를 냈습니다. 컴퓨터가 이겼습니다.\n 컴퓨터 '+str(com)+' : '+str(user)+' 사용자')

       elif comn == 2 and usern == '보':
         
         user += 1
         easygui.msgbox('컴퓨터는 바위를 냈습니다. 당신이 이겼습니다.\n 컴퓨터 '+str(com)+' : '+str(user)+' 사용자')

       elif comn == 3 and usern == '가위':
         
         user += 1
         easygui.msgbox('컴퓨터는 보를 냈습니다. 당신이 이겼습니다.\n 컴퓨터 '+str(com)+' : '+str(user)+' 사용자')

       elif comn == 3 and usern == '바위':
         
         com += 1
         easygui.msgbox('컴퓨터는 보를 냈습니다. 컴퓨터가 이겼습니다.\n 컴퓨터 '+str(com)+' : '+str(user)+' 사용자')

       game += 1
          
        

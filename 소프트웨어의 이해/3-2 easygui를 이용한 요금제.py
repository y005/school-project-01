import easygui

name = easygui.enterbox("이름을 입력하세요")
talk = easygui.enterbox("음성 통화 시간(분)을 입력하세요")
mes = easygui.enterbox("문자 건수를 입력하세요")
data = easygui.enterbox("데이터 사용량(MB)을 입력하세요")

talk = int(talk)
mes = int(mes)
data = int(data)

if talk > 120:
    talk = (talk - 120)* 60 * 1.98
else:
    talk = 0
if mes > 200:
    mes = (mes - 200) * 22
else:
    mes = 0
if data > 800:
    data = (data - 800)*55
else:
    data = 0
    
price = 37400 + talk + mes + data

inf = "     ======"+name+"""님의 4월 이용요금======\n
      32요금제 기본요금:""" + str(37400)+"""원\n 
      음성통화 초과 요금: """ + str(talk)+"""원\n
      문자 초과 요금: """+ str(mes)+"""원\n
      데이터 사용 초과 요금: """+ str(data)+"""원\n
      =============================\n
      총요금:"""+ str(price)+"원"  



easygui.msgbox(inf)







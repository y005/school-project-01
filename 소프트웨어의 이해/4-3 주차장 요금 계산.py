import math

print("숙명여자대학교 4월 단기 주차장\n(24시간 이상 주차하실 수 없습니다.)")
car = input("차량 번호를 입력하세요: ")


while True:
     come = int(input("들어온 시간을 입력하세요(0~23): "))
     comem  = int(input("들어온 분을 입력하세요(0~59): "))
     out = int(input("나간 시간을 입력하세요(0~23): "))
     outm = int(input("나간 분을 입력하세요(0~59): "))
     if come > 23 or come < 0  or comem > 59 or comem < 0 or out > 23 or out < 0 or outm < 0 or outm > 59:
        print("입력 오류입니다. 범위를 맞추어 다시 입력하세요.")
     else:
        break

if come <= out:                         #하루 넘지 않고 
    hour = out - come
    m = outm - comem
    if m < 0:
        hour -= 1
        m += 60

    time = hour * 60 + m

    if time < 30:
        fee = 1500                    
    elif time >= 30 and math.ceil((time - 30)/15) <= 17:
        fee = math.ceil((time - 30)/15) * 600 + 1500
    elif math.ceil((time - 30)/15) >= 18:
        fee = 1200

    
    
else:                                    #하루 넘어서
     if comem == 0:
         hour = 24 - come
         m = comem   
        
     if comem != 0:
         hour = 24 - come - 1
         m = 60 - comem

     time1 = hour * 60 + m

     if time1 < 30:
        fee = 1500                    
     if time1 >= 30 and math.ceil((time1 - 30)/15) <= 17:
        fee = math.ceil((time1 - 30)/15) * 600 + 1500
     if math.ceil((time1 - 30)/15) >= 18:
        fee = 12000


     hour = out
     m = outm
     time2 = hour * 60 + m

     if time2 < 30:
        fee += 1500                    
     if time2 >= 30 and math.ceil((time2 - 30)/15) <= 17:
        fee = fee + math.ceil((time2 - 30)/15) * 600 + 1500
     if math.ceil((time2 - 30)/15) >= 18:
        fee += 12000
 
     time = time1 + time2
     hour = time // 60
     m = time % 60

print("'",car,"' 차량 주차료 명세서\n"
      ,"입차 시간 : ",come,"시",comem,"분\n"
      ,"출차 시간: ",out,"시",outm,"분\n"
      ,"주차 시간: ",hour,"시간",m,"분(",time,"분)\n"
      ,"주차 요금: ",fee,"원") 

money = 100000
print("숙명은행 ATM")
name = input("계좌 소유자 이름을 입력하세요.: ")
while True:
    print("1. 입금\n2. 출금\n3. 잔액 확인\n4. 종료\n")
    select = input("선택: ")

    if select == "1":
        put = int(input("입금액: "))
        money += put
        print(put,"원이 입금되었습니다.")  
    elif select == "2":
        out = int(input("출금액: "))
        if out > money:
          print("잔액이 부족합니다. 인출이 이루어지지 못했습니다.")
        elif out < 0:
          print("출금액을 정확히 입력하세요.")
        else:
          print(out,"원이 인출되었습니다.")
          money -= out
    elif select == "3":
        print(name + "님의 현재 잔액은",str(money) + "원 입니다.") 
    elif select == "4":
        break
    
print("이용해 주셔서 감사합니다.")

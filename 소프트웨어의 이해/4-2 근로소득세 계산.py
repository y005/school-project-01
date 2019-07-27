while True:
    money = input("과세 표준 금액을 입력하세요. (만원 단위): ")

    if len(money) == 0:
        break
    
    if int(money) <= 1200:
        tax = int(money)*0.06
    elif 1200 < int(money) <= 4600:
        tax = 72 + (int(money) -1200)*0.15
    elif 4600 < int(money) <= 8800:
        tax = 582 + (int(money) - 4600)*0.24
    elif 8800 < int(money) <= 30000:
        tax = 1590 + (int(money) - 8800)*0.35
    else:
        tax = 9010 + (int(money) - 30000)*0.38
    print("근로소득세는",tax,"만원 입니다.")
    
print("프로그램을 종료합니다.")    

food = float(input("음식 가격을 입력하세요: "))
tax = 10.5
tip = 15

foodprice = food*(100 +tax + tip)/100
print("지불 총액은",foodprice,"원 입니다.")

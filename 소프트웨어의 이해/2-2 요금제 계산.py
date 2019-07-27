name =input("이름을 입력하세요: ")
call = int(input("음성통화 시간(초)를 입력하세요: "))

data = int(input("데이터 사용량(MB)을 입력하세요: "))

price = call*1.98+data*55+12100
print(name,"님의 3월 이용 금액은",price,"원 입니다.")

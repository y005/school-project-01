import random

name = input("이름을 입력하세요: ")
time = int(input("도전 횟수를 입력하세요: "))
answer = random.randint(1,100)
num = 0
rule = name+"님 "+str(time)+"번째 추측 값을 입력해주세요(1~100): "
while num != answer and time > 0:
    num = int(input(rule))
    if num < answer:
        print("정답보다 작습니다.")
    elif num > answer:
        print("정답보다 큽니다.")
    time = time - 1
    print(time,"번 기회가 남았습니다")
if num == answer:
    print("정답입니다.")
else:
    print("더 이상 기회가 없습니다. 정답은",answer)

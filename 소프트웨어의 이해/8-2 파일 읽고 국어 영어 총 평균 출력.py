memo = input("불러올 파일 이름을 입력하세요: ")

f = open(memo)
sum1 = 0
sum2 = 0
score = []
scoreRead1 = []
scoreRead2 = []

while True:

    line = f.readline()
    if len(line) == 0:
        break
    line = line.strip()
    score1 = line.split(' ')
    score += score1
            
f.close()

n = len(score)

for x in range(0,int(n/2)):

     scoreRead1.append(score[2*x])
     scoreRead2.append(score[2*x + 1])     

     sum1 = int(scoreRead1[x]) + sum1        
     sum2 = int(scoreRead2[x]) + sum2        
    
ave1 = sum1/(n/2)
ave2 = sum2/(n/2)
ave3 = (sum1 + sum2)/n

print("============================")
print("국어 평균: %.2f" %ave1)
print("영어 평균: %.2f" %ave2)
print("총 평균: %.2f" %ave3)

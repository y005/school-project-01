scoreRead = []
memo = input("불러올 파일 이름을 입력하세요: ")
f = open(memo)
su = 0
best = 0
while True:
    line = f.readline()
    if len(line) == 0:
            break
    line = line.strip()
    scoreRead.append(int(line))
        
for x in scoreRead:
    
    print(x)
    su = x + su
    if x > best:
        best = x
    else:
        best = best

f.close()
        

n = len(scoreRead)     
ave = su/n

print("=====================")
print("평균: ", ave)
print("최고점: ",best)

scores = []
rank = 1
samescorecount = 0
temp = 0

while True:
  grade = input('숫자를 입력해 주세요. 끝내시려면 엔터키를 눌러주세요 \n') 

  if len(grade) == 0:
     if len(scores) == 0:
          print("숫자가 존재하지 않습니다")
          continue 
     break

  else:
     grade = int(grade)
     scores.append(grade)
     continue

scores.sort(reverse = True)

print(scores)

if len(scores)%2 == 0:
    mid = scores[int(len(scores)/ 2)] + scores[int(len(scores)/ 2 - 1)]
else:
    mid = scores[int((len(scores)+1)/2) - 1]

print('최대값' , scores[0],'\n최소값', scores[len(scores)-1],'\n중간값', mid)

print("점수판")


for x in scores:
    if x == scores[0]:

        temp = x
        rank = rank
        samescorecount += 1

    else:

        if temp == x:
            temp = x
            rank = rank
            samescorecount += 1
            
        else:
            temp = x
            rank += samescorecount
            samescorecount = 1

    print(rank,'위', x,'점')
    
    

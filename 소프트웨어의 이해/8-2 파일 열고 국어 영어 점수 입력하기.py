
name = input("저장할 파일 이름을 입력하세요: ")
def write_file():
    f = open(name,'w')
    for x in mymemo:
        msg = str(x) + '\n'
        f.write(msg)
    f.close()
    
mymemo = []
while True:
    print("국어와 영어 점수를 입력해주세요.\n예) 90 85")
    items = (input())
    if len(items) == 0:
        break
    mymemo.append(items)
    
write_file()
print(name," 저장 완료")




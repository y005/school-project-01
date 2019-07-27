
name = input("파일명을 입력하세요: ")
def write_file():
    f = open(name,'w')
    for x in mymemo:
        msg = str(x) + '\n'
        f.write(msg)
    f.close()
    
mymemo = []
while True:
    print("점수를 입력해주세요. 끝내시려면 엔터키 두 번 눌러주세요.")
    items = (input())
    if len(items) == 0:
        break
    mymemo.append(int(items))
    
write_file()
print(name," 저장 왼료")

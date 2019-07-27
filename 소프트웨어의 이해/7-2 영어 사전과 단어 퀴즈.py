dic = {}
count = 0

while True:
    key = dic.keys()
    value = dic.values()

    print('   영한사전\n1.단어 입력\n2.단어 조회/수정\n3.단어 삭제\n4.전체 단어 출력\n5.단어 시험\n6.종료')

    choice = int(input('선택: '))

    if choice == 1:

        print('저장할 단어를 입력하세요. 끝내시려면 엔터키를 눌러주세요.')

        while True:
            word = input('단어: ')

            if len(word) == 0:
                break

            elif word in key:
                print('이미 존재하는 단어입니다.')
                
            else:
                mean = input('뜻: ')
                dic[word] = mean
                

    elif choice == 2:
        word = input('찾으실 단어를 입력하세요.\n단어: ')

        if word  not in key:
            print(word, '은(는) 사전에 존재하지 않습니다.')
            

        else:
            print(word,':',dic[word])
            answer = input('수정하시겠습니까? [Y/N]: ')
            if answer == 'Y':
                mean = input(word + ': ')
                dic[word] = mean
                
            if answer == 'N':
                continue

    elif choice == 3:
        word = input('삭제할 단어를 입력하세요.\n 단어: ')
        if word  not in key:
            print(word, '은(는) 사전에 존재하지 않습니다.')
            continue

        else:
            del dic[word]
            print('삭제되었습니다.')
            continue

    elif choice == 4:
        for x in key:
            print(x,'             ',dic[x])
        
    
    elif choice == 5:
        if len(key) == 0:
            print('단어가 존재하지 않아 시험이 불가능합니다.')

        else:   
            for x in key:
                print(x)
                answer = input(':')
                if  answer == dic[x]:
                    print('정답입니다.')
                    count += 1

                else:
                    print('오답입니다.')

            print('총 ',count,'개 정답입니다.')       

    elif choice == 6:
        print('이용해 주셔서 감사합니다.')
        break
     
    else:
        print('잘못 입력했습니다. 다시 선택해주세요.')
        
    

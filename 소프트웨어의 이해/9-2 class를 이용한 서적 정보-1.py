class Book():

    __counter = 0

    def __init__(self, writer, title, price, page):
        self.writer1 = writer
        self.title1 = title
        self.price1 = price
        self.page1 = page
        Book.__counter += 1

    def  __del__(self):
        Book.__counter -= 1

    def print_book(self):
        print('저자 : %s\n제목 : %s\n가격 : %s\n페이지 수 : %s\n'%(self.writer1,self.title1, self.price1, self.page1))

    def printCount():
        print('전체  책의 개수는 %d개 입니다' %Book.__counter)

list = []
while True:
    choice = input('1. 책 추가\n2. 책 삭제\n3. 전체 책 출력\n4. 종료\n 선택 : ')

    if choice == '1':
        writer0 = input('작가: ')
        title0 = input('제목: ')
        price0 = input('가격: ')
        page0 = input('페이지수: ')

        book = Book(writer0, title0, price0, page0)

        list.append(book)
        
    elif choice == '2':
        index = int(input('삭제할 책의 인덱스를 입력하세요. : '))

        del(list[index])
        

    elif choice == '3':
        for x in list:
            x.print_book()

        Book.printCount()
        
    elif choice == '4':
        print('이용해주셔서 감사합니다.')
        break


    else:
        print('잘못 입력했습니다.')
                 
            

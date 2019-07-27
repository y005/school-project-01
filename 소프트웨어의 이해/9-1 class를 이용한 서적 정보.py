
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
        print('저자 : %s\n제목 : %s\n가격 : %s\n페이지 수 : %s'%(self.writer1,self.title1, self.price1, self.page1))

    def printCount():
        print('총 %d권' %Book.__counter)


class Textbook(Book):

    def __init__(self, writer, title, price, page, subject, major, year, semester):

        self.subject1 = subject
        self.major1 = major
        self.year1 = year
        self.semester1 = semester

        Book.__init__( self, writer, title, price, page)

        #super을 이용해 쓰면 self라는  객체 지정을 따로 표기하지 않아도 된다
        #super().__init__( writer, title, price, page)

    def print_book(self):
        super().print_book()
        print('교과목명 : %s\n전공 : %s\n연도 : %s\n학기 : %s' %(self.subject1,self.major1, self.year1, self.semester1))

    def change_subject(self,subject):
        self.subject1 = subject

    def change_year(self, year):
        self.year1 = year

    def change_semester(self, semester):
        self.semester1 = semester   


book1 = Book('이기주', '언어의 온도','1800원','308쪽')
book2 = Book('조남주','82년 생 김지영','13000원','192쪽')
book3 = Book('히가시노 게이고','나미야 잡화점의 기적','14800원','456쪽')
book4 = Book('공지영','할머니는 죽지 않았다.','12000원','272쪽')
text1 = Textbook('유석종, 이상규, 창명모','Python 프로그래밍의 이해', '18000원','320쪽', '프로그래밍의 이해','소프트웨어학부','2017','1학기')
text2 = Textbook('심준호','데이터베이스프로그래밍','13000원','256쪽', '데이터베이스프로그래밍', '컴퓨터과학전공', '2016','1학기')
text3 = Textbook('Poster Provost and Tom Fawcett','Data Science for Business','37400원','414쪽','데이터사이언스개론 ','소프트웨어융합전공','2018','2학기')  
text4 = Textbook('창병모','유닉스 리눅스 사용해서 프로그래밍까지','24000원','466쪽','리눅스시스템','소프트웨어학부','2014','2학기')

book1.print_book()
print('                               ')
book2.print_book()
print('                               ')
book3.print_book()
print('                               ')
book4.print_book()
print('                               ')
text1.print_book()
print('                               ')
text2.print_book()
print('                               ')
text3.print_book()
print('                               ')
text4.print_book()
print('                               ')

Book.printCount()

del(book3)

text1.change_subject('소프트웨어의 이해')

text2.change_year('2017')

text3.change_semester('1학기')

del(text4)


print('=====================수정된 목록====================')

text1.print_book()
print('                               ')
text2.print_book()
print('                               ')
text3.print_book()
print('                               ')


Book.printCount()



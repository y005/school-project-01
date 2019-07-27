# Frog 게임

from tkinter import *
import random
import time

# Frog 클래스
class Frog:

    #초기화 메소드
    def __init__(self, canvas, car1, car2, car3, color):

        self.i = 0
        self.speed1 = 'normal'
        self.speed2 = [1,2,3]
        
        self.canvas = canvas
        self.car1 = car1
        self.car2 = car2
        self.car3 = car3
        self.color = color

        self.id = canvas.create_oval(10,10,50,50, fill= color)        
        self.canvas.move(self.id, 250, 420)

        self.x = 0
        self.y = 0
        self.step = 60
        self.score = 0
        self.life = 5

        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Up>', self.move_up)
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)
        self.canvas.bind_all('<space>',self.change_speed) 

        canvas.create_text(245,40,text = "speed: "+ self.speed1,tag ='speed')  
        canvas.create_text(90,40,text = "score : "+str(self.score))
        canvas.create_text(400,40,text = "life : "+str(self.life))  

    #자동차 스피드 표시
    def change_speed(self,evt):

        self.i += 1
        self.i = (self.i) % 3

        if self.i == 1:
            self.speed1 = 'fast'
            
        elif self.i == 2:
            self.speed1 = 'faster' 

        else:
            self.speed1 = 'normal' 

        canvas.delete('speed')
        canvas.create_text(245,40, text = "speed: "+ self.speed1, tag = 'speed')  

        self.car1.x = self.car1.speed * self.speed2[self.i] 
        self.car2.x = self.car2.speed * self.speed2[self.i] 
        self.car3.x = self.car3.speed * self.speed2[self.i] 


    # 충돌 검사 메소드    
    def hit_car(self, pos):
        car_pos = self.canvas.coords(self.car1.id)
        if pos[2] >= car_pos[0] and pos[0] <= car_pos[2]:
            if pos[3] >= car_pos[1] and pos[1] <= car_pos[3]:
                return True

        car_pos = self.canvas.coords(self.car2.id)
        if pos[2] >= car_pos[0] and pos[0] <= car_pos[2]:
            if pos[3] >= car_pos[1] and pos[1] <= car_pos[3]:
                return True

        car_pos = self.canvas.coords(self.car3.id)
        if pos[2] >= car_pos[0] and pos[0] <= car_pos[2]:
            if pos[3] >= car_pos[1] and pos[1] <= car_pos[3]:
                return True
            
        return False
    
    # 화면 출력 메소드    
    def draw(self):    
        self.canvas.move(self.id, self.x, self.y)
        self.x = 0
        self.y = 0
        
        pos = self.canvas.coords(self.id)
        
        if pos[0] <= 0:
            self.canvas.move(self.id, self.step/2, self.y)
            self.x = 0
        elif pos[2] >=self.canvas_width:
            self.canvas.move(self.id, -self.step/2, self.y)
            self.x = 0
        elif pos[1] < 60:    # frog made it
            self.score =self.score +10
            canvas.create_rectangle(10,10,200,60, outline=tk.cget("bg"), fill=tk.cget("bg"))  
            canvas.create_text(90,40,text = "score : "+str(self.score))               
            self.canvas.move(self.id, 250-pos[0],420)
 
        if self.hit_car(pos) == True :   # car hit the frog
            self.life = self.life -1
            if self.life <=0:
                canvas.create_text(250,260, text = "G A M E  O V E R")
            else:    
                canvas.create_rectangle(300,10,550,60, outline=tk.cget("bg"), fill=tk.cget("bg"))  
                canvas.create_text(400,40,text = "life : "+str(self.life))
                self.canvas.move(self.id, 250-pos[0],430-pos[1])                
	   
# 위, 왼쪽, 오른쪽 이동 메소드
    def move_up(self, evt):
        self.y = -self.step
    def move_left(self, evt):
        self.x = -self.step/2   
    def move_right(self, evt):
        self.x = self.step/2

#자동차 클래스
class Car:

    # 자동차 초기화 메소드
    def __init__(self, canvas, x, y, color, speed):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10,10,100,60, fill = color)
        self.canvas.move(self.id, x, y)
        self.speed = speed
        self.x = speed
        self.y = 0
    
    # 자동차 출력 메소드
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        
        pos = self.canvas.coords(self.id)
        if pos[0] <= -100:
            self.canvas.move(self.id, 600, 0)
        elif pos[2] >= 700: 
            self.canvas.move(self.id, -700, 0)            

tk = Tk()
tk.title("Frog")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
tk.update()

car1 = Car(canvas, 10, 60, "red", 5)
car2 = Car(canvas, 500, 180, "blue", -3)
car3 = Car(canvas, 10, 300, "yellow", 1)
frog = Frog(canvas, car1, car2, car3, "green")
             

while 1:  
    if frog.life >= 0:
        car1.draw()
        car2.draw()
        car3.draw()
        frog.draw()
    
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

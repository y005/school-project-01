import math

fx = int(input("첫 번째 x좌표 입력: "))
fy = int(input("첫 번째 y좌표 입력: "))
sx = int(input("두 번째 x좌표 입력: "))
sy = int(input("두 번째 y좌표 입력: "))

x = sx - fx
y = sy - fy

dx = math.pow(x,2)
dy = math.pow(y,2)

z = dx + dy


s = math.sqrt(z)

print("두 점 사이의 거리: ",s)

#p76-1번
'''
옳은 변수
 abc, import_var, test, k31
틀린변수
  3ab - 첫자 숫자
  a b  -  중간에 빈공간이 있음
  import - 예약어
  temp# - 특수문지사용
'''

#p77-4번
'''
a = 3
b = 2
c = 1
a = a + 1
b = b
c = a + b
c = c + 1

print(a, b, c)  
  
'''


#p78-7번
'''
s = "#"
print(s * 3)
print(s * 5)
'''

#p82-6번
'''
a = int(input("정수1 : "))
b = int(input("정수2 : "))
c = int(input("정수3 : "))
sum = a + b + c
avg = sum / 3
print("정수1 :", a, "정수2 :", b, "정수3 :", c)
print("합 :", sum, "평균 :", avg)
'''

#p83-8번
'''
import turtle
turtle.shape("turtle")
turtle.up()
x = int(input("x 좌표 : "))
y = int(input("y 좌표 : "))
turtle.goto(x, y)
turtle.stamp()
x = int(input("x 좌표 : "))
y = int(input("y 좌표 : "))
turtle.goto(x, y)
turtle.stamp()
x = int(input("x 좌표 : "))
y = int(input("y 좌표 : "))
turtle.goto(x, y)
turtle.stamp()
'''

#p84-9번
'''
import turtle
radius = int(input("반지름 : "))
length = int(input("진행 : "))
turtle.shape("turtle")
turtle.circle(radius)
turtle.forward(length)
turtle.circle(radius)
turtle.forward(length)
turtle.circle(radius)
turtle.forward(length)
'''







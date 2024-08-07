'''
1번
abc=1        O
3ab=1        X
a b=1        X
import=1     O
import_var=1 O
test=1       O
temp#=1      X
k31 =1       O
'''
'''
4번
a = 3
b = 2
c = 1
a = a+1
b = b
c = a+b
c = c+1
a=4 이고 b=2 이고 c=7 이다.
'''
'''
7번
s="#"
print(s*3)
print(s*4)
'''
'''
6번
a=int(input("정수1: "))
b=int(input("정수2: "))
c=int(input("정수3: "))
print("정수1: ",a , "정수2: ",b, "정수3: ",c)
sum=a+b+c
print("합: ",sum,"평균",sum/3)
'''
'''
8번
import turtle
turtle.shape("turtle")
x=int(input("x좌표: "))
y=int(input("y좌표: "))
turtle.goto(x,y)
turtle.up()
turtle.stamp()

x=int(input("x좌표: "))
y=int(input("y좌표: "))
turtle.goto(x,y)
turtle.up()
turtle.stamp()

x=int(input("x좌표: "))
y=int(input("y좌표: "))
turtle.goto(x,y)
turtle.up()
turtle.stamp()
'''
'''
9번
import turtle
turtle.shape("turtle")
radius = int(input("반지름: "))
length = int(input("진행: "))
for i in range(3):
    turtle.circle(radius)
    turtle.forward(length)
'''


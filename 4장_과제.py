#p99-2번
'''
a = int(input("숫자1 : "))
b = int(input("숫자2 : "))
print(a, "/", b, "=", a / b)
print(a, "//", b, "=", a // b)
print(a, "%", b, "=", a % b)
'''

#p100-5번
'''
print(3+(4/2)+1)
print((1+2)/(2+4))
print((3*2)/(4-(2/3)))

#또는

a = 3+(4/2)+1   #연산부분은 따로 계산함
print(a)
b = (1+2)/(2+4)
print(b)
c = (3*2)/(4-(2/3))
print(c)
'''

#p101-7번
'''
sco1 = int(input("국어 : "))
sco2 = int(input("영어 : "))
sco3 = int(input("수학 : "))
total = sco1 + sco2 + sco3
average = total / 3
print("총점 :", total)
print("평균 :", average)
'''

#p103-13번
'''
length = int(input("길이 : "))
import turtle
turtle.shape("turtle")
turtle.forward(length*1)
turtle.goto(0, 0)
turtle.right(45)
turtle.forward(length*2)
turtle.goto(0, 0)
turtle.right(45)
turtle.forward(length*4)
turtle.goto(0, 0)
turtle.right(45)
turtle.forward(length*8)
turtle.goto(0, 0)
turtle.right(45)
turtle.forward(length*16)
'''


#p105-5번
'''
sec = int(input("초 : "))
minute = sec // 60
second = sec % 60
print(sec, "초 = ", minute, "분", second, "초")
'''

#p106-11번
'''
chicken = int(input("닭 : "))
rabbit = int(input("토끼 : "))
pig = int(input("돼지 : "))
leg = chicken * 2 + rabbit * 4 + pig * 4
print("다리 합계 :", leg)
'''

#p107-13번
'''
opnd1 = int(input("피연산자1 : "))
opnd2 = int(input("피연산자2 : "))
v3 = opnd1 // 100
v2 = opnd1 // 10 % 10
v1 = opnd1 % 10
print(opnd1, "*", opnd2)
print("=", "(", v3, "+", v2, "+", v1, ")", "*", opnd2)
print("=", v3, "*", opnd2, "+", v2, "*", opnd2, "+", v1, "*", opnd2)
print("=", v3*opnd2, "+", v2*opnd2, "+", v1*opnd2)
print("=", opnd1*opnd2)

#또는

opnd1 = int(input("피연산자1 : "))
opnd2 = int(input("피연산자2 : "))
v3 = opnd1 // 100
v2 = opnd1 % 100 // 10  #이부분이 다름
v1 = opnd1 % 10
print(opnd1, "*", opnd2)
print("=", "(", v3, "+", v2, "+", v1, ")", "*", opnd2)
print("=", v3, "*", opnd2, "+", v2, "*", opnd2, "+", v1, "*", opnd2)
print("=", v3*opnd2, "+", v2*opnd2, "+", v1*opnd2)
print("=", opnd1*opnd2)
'''






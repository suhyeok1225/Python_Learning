#1
'''
a=int(input("숫자1: "))
b=int(input("숫자2: "))
div=a/b
print(div)
share=a//b
print(share)
rmd=a%b
print(rmd)
'''
#2
'''
a=3+4/2+1
print(a)
b=1+2/2+4
print(b)
c=3*2/4-2/3
print(c)
'''
#3
'''
sco1=int(input("국어: "))
sco2=int(input("수학: "))
sco3=int(input("영어: "))
sum=sco1+sco2+sco3
print("총점: ",sum)
age=(sco1+sco2+sco3)/3
print("평균: ",age)
'''
#4
'''
import turtle
turtle.shape("turtle")
length=int(input("길이: "))

turtle.forward(length*1)
turtle.right(45)
turtle.goto(0,0)

turtle.forward(length*2)
turtle.goto(0,0)
turtle.right(45)

turtle.forward(length*4)
turtle.goto(0,0)
turtle.right(45)

turtle.forward(length*8)
turtle.goto(0,0)
turtle.right(45)

turtle.forward(length*16)
'''
#5
'''
second=int(input("초: "))
minute=second//60
second=second%60
print(minute,"분",second,"초")
'''
#6
'''
chi=int(input("닭: "))
rib=int(input("토끼: "))
pig=int(input("돼지: "))
        
chi_leg=chi*2
rib_leg=rib*4
pig_leg=pig*4
sum=chi_leg+rib_leg+pig_leg
print("다리합계: ",sum)        
'''
#7
'''
opnd1 =int(input("피연산자1 : "))
opnd2 =int(input("피연산자2 : "))

num1=opnd1//100
num2=opnd1//10%10
num3=opnd1//1%10

sum1 = num1*opnd2*100
sum2 = num2*opnd2*10
sum3 = num3*opnd2

print(sum1+sum2+sum3)
'''

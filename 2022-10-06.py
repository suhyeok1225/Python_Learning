#1
'''
num=int(input("정수입력: "))
if num<100:
    num=num*0.9
else:
    num=num*1.1
print(num)    
'''
#2
'''
num=int(input("1-삼각형 넓이  2-원의 넓이  3-사다리꼴의 넓이 '선택': "))
if num == 1:
    a=int(input("밑변 입력: "))
    h=int(input("높이 입력: "))
    area=(a*h)/2
    print("삼각형의 넓이 =",area)
elif num == 2:
    r=int(input("반지름 입력: "))
    area=(r**2)*3.14
    print("원의 넓이 = ",area)
elif num == 3:
    a=int(input("밑변 입력: "))
    b=int(input("윗변 입력: "))
    h=int(input("높이 입력: "))
    area=((a+b)*h)/2
    print("사다리꼴의 넓이 =",area)
else:
    print("다시 입력: ")
'''
#3
'''
for i in [1,2,3,4,5]:
    print("파이썬")
'''
#4
'''
for i in [1,2,3,4,5]:
    print("파이썬",i)
'''
#5
'''
s=0
for i in [1,2,3,4,5]:
    s=s+i
print("s:",s)
'''
#6
'''
s=0
for i in [1,2,3,4,5]:
    s=s+i
    print("i:",i,"s:",s)
print("s:",s) 
'''
#7
'''
s=0
for i in[5,4,3,2,1]:
    s=s+i
print("s:",s)   
'''
#8
'''
for i in range(3):
        num=int(input("1-삼각형 넓이  2-원의 넓이  3-사다리꼴의 넓이 '선택': "))
        if num == 1:
            a=int(input("밑변 입력: "))
            h=int(input("높이 입력: "))
            area=(a*h)/2
            print("삼각형의 넓이 =",area)
        elif num == 2:
            r=int(input("반지름 입력: "))
            area=(r**2)*3.14
            print("원의 넓이 = ",area)
        elif num == 3:
            a=int(input("밑변 입력: "))
            b=int(input("윗변 입력: "))
            h=int(input("높이 입력: "))
            area=((a+b)*h)/2
            print("사다리꼴의 넓이 =",area)
        else:
            print("다시 입력: ")
'''

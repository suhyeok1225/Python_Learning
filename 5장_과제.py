#p131-2번
'''
print(3 > 2 or 2 < -1)
print(2 <- 1 or 3 > 2)
print(2 <- 1 or 3 < 2)
print(3 > 2 and 2 <- 1)
print(2 <- 1 and 3 > 2)
print(3 > 2 and 2 >- 1)
print(not (3 > 2 and 2 <- 1))
print(not (3 > 2 and 2 >- 1))
'''


#p132-4번
'''
num = int(input("정수 : "))
if num >= 10 and num <= 30:
    print(num)
else:
    print("범위를 벗어난 수")
'''



#p133-7번
'''
sco1 = int(input("국어 : "))
sco2 = int(input("영어 : "))
sco3 = int(input("수학 : "))
total = sco1 + sco2 + sco3
average = total / 3
if average >= 80:
    rating = "잘함"
elif average >= 70:
    rating = "보통"
else:
    rating = "미흡"
print("총점 :", total)
print("평균 :", average)
print("평가 :", rating)
'''



#p134-10번
'''
a = int(input("a : "))
b = int(input("b : "))
if a % b == 0:
    print("배수")
else:
    print("배수가 아님")
'''




#p137-5번
'''
a = 5
b = 3
ch = input("연산자 : ")
if ch == '+':
    tmp = a + b
elif ch == '-':
    tmp = a - b
elif ch == '*':
    tmp = a * b
elif ch == '/':
    tmp = a / b
print(a, ch, b, '=', tmp)
'''


#p137-6번
'''
ph = int(input("pH : "))
if ph >= 0 and ph <= 4:
    print("강산성")
elif ph >= 5 and ph <= 6:   # ph <= 6 도 가능
    print("약산성")
elif ph == 7:
    print("중성")
elif ph >= 8 and ph <= 9:   # ph <= 9 도 가능
    print("약염기성")
elif ph >= 10 and ph <= 14: # ph <=14 도 가능
    print("강염기성")
'''


#p139-9번
'''
ppower = int(input("전 달 전력량 : "))
cpower = int(input("이번 달 전력량 : "))
powercomsum = cpower - ppower
if powercomsum < 0:
    print("전력량 입력 오류")
else:
    if powercomsum < 200:
        brate = 910
        prate = 93.3
    elif powercomsum <= 400:
        brate = 1600
        prate = 187.9
    else:    
        brate = 7300
        prate = 280.6
    ebill = brate + powercomsum * prate
    print("이번 달 전력 사용량 =", powercomsum)
    print("전기요금 =", ebill)
'''


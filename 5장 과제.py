#1
'''
3>2 or 2<-1
2<-1 or 3>2
2<-1 or 3<2
3>2 and 2<-1
2<-1 and 3>2
3>2 and 2>-1
not(3>2 and 2<-1)
not(3>2 and 2>-1)
'''
#2
'''
num=int(input("정수: "))
if num>=10 and num<=30:
    print(num)
else:
    print("범위를 벗어 난 수")
'''
#3
'''
kor=int(input("국어: "))
eng=int(input("영어: "))
mat=int(input("수학: "))
sum=kor+eng+mat
print("총점:",sum)
avg=(kor+eng+mat)/3
print("평균:",avg)
if avg>80:
    print("잘함")
elif avg>=70 and avg<=79:
    print("보통")
else:
    print("미흡")
'''
#4
'''
a=int(input("a:"))
b=int(input("b:"))
if a%b==0:
    print("배수")
else:
    print("배수가 아님")
'''
#5
'''
a=5
b=3
opt=int(input("1 - + , 2 - - , 3 - * , 4 - / 선택 "))
if opt==1:
    sum=a+b
    print(sum)
elif opt==2:
    min=a-b
    print(min)
elif opt==3:
    mul=a*b
    print(mul) 
elif opt==4:
    div=a/b
    print(div)
else:
    print("다시 입력 하세요.")
'''
#6
'''
ph=int(input("pt: "))
if ph>=0 and ph<=4:
    print("강산성")
elif ph>=5 and ph<=6:
    print("약산성")
elif ph==7:
    print("중성")
elif ph>=8 and ph<=9:
    print("약염기성")
elif ph>=10 and ph<=14:
    print("강염기성")
else:
    print("다시입력해주세요.")
'''
#7
'''
num1=int(input("전 달 전력량: "))
num2=int(input("이번 달 전력량: "))
if num2<num1:
    print("전력량 입력 오류")
else:
    div=num2-num1
    print("이번 달 전력 사용량=", div)
    if div<=200:
        fee=910+(div*93.3)
        print("전기요금=",fee)
    elif div>=201 and div<=400:
        fee=1600+(div*187.9)
        print("전기요금=",fee)
    else:
        fee=7300+(div*280.6)
        print("전기요금=",fee)
'''
    
    



    
    

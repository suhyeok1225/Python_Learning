#1
'''
num=int(input("정수  입력: "))
if num > 0:
    print("양수")
if num == 0:
    print("0")
if num < 0:
    print("음수")
'''
#2
'''
kor_score =70
if kor_score >=80:
    print("합격입니다.")
else:
    print("불합격 입니다")
'''
#3
'''
kor_score =90
eng_score =85
if kor_score >= 80 and eng_score >=80:
    print("합격입니다.")
else:
    print("불합격입니다.")
'''
#4
'''
kor_score =90
eng_score =85
if kor_score < 80  or eng_score < 80:
    print("합격입니다.")
else:
    print("불합격입니다.")
'''
#5
'''
num=int(input("양의 정수 입력: "))
if num%2 == 0:
    print("짝수")
else:
    print("홀수")
'''    
#6
'''
num=int(input("정수 입력: "))
if num == 0:
    print("0")
elif num > 0:
    print("양수")
else:
       print("음수")
'''
#7
'''
num = -5
if num > 0:
    print("양수")
elif num == 0:
    print("0")
else:
    print("음수")
'''
#8
'''
score=int(input("점수: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >=60:
    print("D")
else:
    print("F")
'''
#9
'''
menu=int(input("1-라면, 2-떡볶이, 3-오뎅, 4-김밥  선택해주세요.": ))
if menu ==1:
    print("라면입니다.")
elif menu == 2:
    print("떡볶이입니다.")
elif menu == 3:
    print("오뎅입니다.")
elif menu == 4:
    print("김밥입니다.")
else:
    print("잘못 입력하셨습니다.")
'''
#10
'''
age=int(input("나이를 입력하세요."))
child=100
gen=1200
if age<7:
    print("유아요금 입니다.")   
    print("당신은",age,"세로",child,"원 입니다")
elif age>=65:
    print("경로요금 입니다.")
    print("당신은",age,"세로",child*3,"원 입니다")
else:
    print("일반요금 입니다.")
    print("당신은",age,"세로",gen,"원 입니다")
'''

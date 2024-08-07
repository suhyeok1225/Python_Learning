#p236-2번
'''
str = input("문자열 : ")
print("개별 문자 출력 : ", end="   ")
for i in range(len(str)):
    print(str[i], end="")
print("")
print("역순 개별 문자 출력 : ", end="")
for i in range(len(str)-1, -1, -1):
    print(str[i], end="")
print("")
'''

#p238-5번
'''
items = { "라면":650, "우유":1100, "콜라":1200, "캔커피":500, "과자":700 }
s = 0
while True:
    it = input("제품명 : ")
    if it == "":
        break
    if it in items:
        s = s + items[it]
        print("[%s:%d] > %d"%(it, items[it], s))
    else:
        print(it, "는 미등록 제품입니다.")
print("총 금액 : ", s)
'''

#p239-7번
'''
import math
num = float(input("실수 : "))
print(num, ":" , math.ceil(num))
print(num, ":" , math.floor(num))
print(num, ":" , math.trunc(num))
'''

#p241-1번
'''
sales = {1:8, 2:6, 3:10, 4:13}
for i in sales:
    print(i, "분기 :", '#' * sales[i], '(', sales[i], ')')
'''



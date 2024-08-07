#P283-4번
'''
quotient = 0
remainder = 0

def div_qr(n1, n2):
    global quotient, remainder
    quotient = n1 // n2
    remainder = n1 % n2

num1 = int(input("정수1 : "))
num2 = int(input("정수2 : "))
div_qr(num1, num2)
print("몫:", quotient, "나머지:", remainder)
'''

#P284-5번
'''
def div_qr(n1, n2):
    quotient = n1 // n2
    remainder = n1 % n2
    return (quotient, remainder)

num1 = int(input("정수1 : "))
num2 = int(input("정수2 : "))
(q, r) = div_qr(num1, num2)
print("몫:", q, "나머지:", r)
'''

#P284-7번
'''
data = [ 21, 7, 43, 65, 2, 8, 72, 52, 9 ]
for i in range( len(data)-1,-1,  -1):
    print(data[i], end=" ")
print("")

'''

#287-2번
'''
data = [ 21, 7, 43, 65, 2, 8, 72, 52, 9 ]
search = int(input("찾을 배수 : "))
find = len(data)
for i in range(len(data)):
    if data[i] % search == 0:
        print("위치 :", i, "값 :", data[i])
        find = i
        continue
if find == len(data):
    print("찾지 못함")
'''


#288-6번
'''
data = [ [21, 7, 43, 65], [2, 8, 72, 52] ]
print("행렬")    
for i in range(len(data)):
    for j in range(len(data[0])):
        print(data[i][j], end=" ")
    print("")
print("")    
print("전치행렬")
for j in range(len(data[0])):
    for i in range(len(data)):
        print(data[i][j], end=" ")
    print("")
'''

#289-8번
'''
data = [ [10, 20, 30, 40, 0],     [50, 60, 70, 80, 0],
         [90, 100, 110, 120, 0],  [130, 140, 150, 160, 0],
         [170, 180, 190, 200, 0], [0, 0, 0, 0, 0] ]
lenr = len(data) - 1
lenc = len(data[0]) - 1
for i in range(lenr):
    for j in range(lenc):
        data[i][lenc] = data[i][lenc] + data[i][j]
        data[lenr][j] = data[lenr][j] + data[i][j]
        print(data[i][j], end=" ")
    print(data[i][lenc])
for j in range(lenc):
    data[lenr][lenc] = data[lenr][lenc] + data[lenr][j]
    print(data[lenr][j], end=" ")
print(data[lenr][lenc])
'''

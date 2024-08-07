#P320-6번
'''
str = "python"
for i in range(1, len(str)+1):
    print("%6s"%str[0:i])
'''
# 또는
'''
str = "python"
for i in range(1, len(str)+1):
    print("%s%s"%(" "*(len(str)-i),str[0:i]))
'''

#P321-8번
'''
str1 = input("문자열1 : ")
str2 = input("문자열2 : ")
if len(str1) > len(str2):
    longstr = str1
else:
    longstr = str2
print("긴 문자열 =", longstr)
'''

#P321-9번
'''
str = input("문자열 : ")
if str.isdigit():
    tmpstr = "숫자"
elif str.isalpha():
    tmpstr = "문자"
elif str.isalnum():
    tmpstr = "숫자/문자"
else:
    tmpstr = "기타 문자"
print("%s로 구성된 문자열"%tmpstr)

'''

#P322-10번
'''
data = []
while True:
    str = input("문자열 : ")
    if str == "":
        break;
    data.append(str)
for i in range(len(data)):
    print(data[i], end=" ")
print("")
'''


#P323-2번
'''
def str2int(s):
    if s.isdigit():
        tmp = int(s)
    else:
        tmp = None
    return tmp

st = input("문자열 : ")
n = str2int(st)
if n != None:
    print("%d"%n)
else:
    print(n)
'''

#P324-4번
'''
list = []
cmd = []
n = int(input("리스트 명령 수 : "))
for i in range(n):
    indata = input("")
    cmd = indata.split()
    if cmd[0] == "append":
        list.append(int(cmd[1]))
    elif cmd[0] == "insert":
        list.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == "remove":
        list.remove(int(cmd[1]))
    elif cmd[0] == "sort":
        list.sort()
    elif cmd[0] == "printout":
        print(list)
'''

#P325-6번
'''
jnymd = input("주민등록번호 연월일 : ")
mm = int(jnymd[2:4])
if mm >= 1 and mm <= 12:
    dd = int(jnymd[4:6])
    if dd >= 1 and dd <= 31:
        mf = int(input("성별 표시 : "))
        print("%s-%d"%(jnymd, mf))
    else:
        print("주민등록번호의 일 형식이 잘못되었습니다.")
else:
    print("주민등록번호의 월 형식이 잘못되었습니다.")

'''


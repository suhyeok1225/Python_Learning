#1
'''
str="python"
for i in range(len(str)):
    print("%6s"%str[0:i+1])
'''
#2
'''
st=input("문자열:")
if st.isdigit():
    print("숫자로 구성된 문자열")
elif st.isalpha():
    print("문자로 구성된 문자열")
elif st.isalnum():
    print("숫자/문자로 구성된 문자열")
else:
    print("다시입력")
'''
#3
'''
data=[]
while True:
    st=input("문자열:")
    data.append(st)    
    if st=="":
        break

for i in range(len(data)):  
    print(data[i])        
'''
#4
'''
def str2int(s):
    if s.isdigit():
        print(s)
    else:
        print(None)
st=input("문자열:")        
str2int(st)
'''
#5
'''
list=[]
cmd=[]
num=int(input("리스트 명령 수:"))
for i in range(num):
    indata=input("리스트 명령:")
    cmd=indata.split()
    if cmd[0]=="append":
        list.append(int(cmd[1]))
    elif cmd[0]=="insert":
        list.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0]=="remove":
        list.remove(int(cmd[1]))
    elif cmd[0]=="sort":
        list.sort()
    elif cmd[0]=="printout":
        print(list)
print(list)
'''
#6
'''
jnymd=input("주민등록번호 년월일:")
if "00" <=jnymd[2:4]>="13":
    print("주민등록번호의 월 형식이 잘못되었습니다.")
elif "00"<=jnymd[4:6]>="32":
    print("주민등록번호의 일 형식이 잘못되었습니다.")
else:
    num=input("성별 표시:")
    print(jnymd,"-",num)    
'''       
    

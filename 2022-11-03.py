#1
'''
engkor_dict=dict()
while True:
    eng=input("영어단어:")
    kor=input("한글단어:")
    if eng==""and kor=="":
        break
    engkor_dict[eng]=kor
print(engkor_dict)    
'''
#2
'''
def comp(seq):
    comp_dict={'A':'T','T':'A','C':'G','G':'C'}
    seq_comp=""
    for char in seq:
        seq_comp=seq_comp+comp_dict[char]
    return seq_comp
def rev(seq):
    seq_rev="".join(reversed(seq))
    return seq_rev
def rev_comp(seq):
    tmp=comp(seq)
    return rev(tmp)

src=input("DNA sequence:")
cnvt=int(input("1(comp), 2(Rev), 3(Rev_Comp):"))
if (cnvt>=1 and cnvt<=3):
    if (cnvt==1):
        rst=comp(src)
    elif(cnvt==2):
        rst=rev(src)
    else:
        rst=rev_comp(src)
    print(src,'->',rst)
else:
    print("잘못입력하셨습니다.")
'''
#3
'''
def comp(seq):
    comp_dict={'A':'T','T':'A','C':'G','G':'C'}
    seq_comp=""
    for char in seq:
        seq_comp=seq_comp+comp_dict[char]
    return seq_comp

def rev(seq):
    seq_rev=""
    n=int(len(seq))-1

    while n>-1:
        seq_rev=seq_rev+seq[n]
        n=n-1
    return seq_rev

def rev_comp(seq):
    tmp=comp(seq)
    return rev(tmp)

src=input("DNA sequence:")
cnvt=int(input("1(comp), 2(Rev), 3(Rev_Comp):"))
if (cnvt>=1 and cnvt<=3):
    if (cnvt==1):
        rst=comp(src)
    elif(cnvt==2):
        rst=rev(src)
    else:
        rst=rev_comp(src)
    print(src,'->',rst)
else:
    print("잘못입력하셨습니다.")
'''
#4
'''
a=[-3,7,9,4,3,4]
print(a[0],abs(a[0]),max(a),min(a),sum(a),pow(2,3))
'''
#5
'''
import math
a=90
r=2
print(math.radians(a))
print(math.degrees(r))
'''
#6
'''
str=input("문자입력:")
print("문자길이:",len(str))
print("첫 번째 문자:",str[0])
print("두 번째 문자:",str[1])
print("마지막 문자:",str[len(str)-1])
'''
#7
'''
items={'공책':325,'연필':427,'지우개':125,'복사지':510}
n=int(input("파악 재고수 기준:"))
for i in items:
    if items[i]<n:
        print(i,":",items[i])
'''    

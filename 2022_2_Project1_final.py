
#사용자에게 IPv4 주소를 입력받는 함수.
def input_ipv4() : 
    f_ipv4 = {'ipv4_1':0, 'ipv4_2':0, 'ipv4_3':0, 'ipv4_4':0}
    print('##Ipv4 주소를 입력해 주세요##')
    for i in f_ipv4 :
        x = int(input('%s번째 ipv4주소 : '%i))
        if 0 <= x and x <= 255 :
            f_ipv4[i] = x
        else :
            print('Error')
            print('0~255까지의 수만 입력 가능합니다.')
            break
    print(f_ipv4)
    return f_ipv4



# 사용자에게 subnet mask를 입력받는 함수.
def input_subnet() : 
    f_subnet = {'subnet_1':0, 'subnet_2':0, 'subnet_3':0, 'subnet_4':0}
    print('##Subnet mask를 입력해 주세요##')
    for i in f_subnet :
        x = int(input('%s번째 Subnet mask : '%i))
        if 0 <= x and x <= 255 :
            f_subnet[i] = x
        else :
            print('Error')
            print('0~255까지의 수만 입력 가능합니다.')
            break
    print(f_subnet)
    return f_subnet



# Ipv4 주소의 Class가 무엇인지 판별해주는 함수.
def f_ip_class(in_ipv4_1) :
    f_class = ''
    if 0 <= in_ipv4_1 and in_ipv4_1 <= 127 :
        f_class = 'A'
    elif 128 <= in_ipv4_1 and in_ipv4_1 <= 191 :
        f_class = 'B'
    elif 192 <= in_ipv4_1 and in_ipv4_1 <= 223 :
        f_class = 'C'
    elif 224 <= in_ipv4_1 and in_ipv4_1 <= 239 :
        f_class = 'D'
    elif 240 <= in_ipv4_1 and in_ipv4_1 <= 255 :
        f_class = 'E' 
    else :
        f_class = ''
    print('Class :', f_class)
    return f_class    



# 입력된 10진수 ip 와 subnet mask주소를 2진수로 변환하는 함수
def ad_binary(ad):
    for i in ad:
        ipv4_binary= ad[i]
        result_binary= format(ipv4_binary,'08b')
        print(result_binary, end =" ")
    print("")
    


# ipv4, subnet mask 를 입력받아, 사용자가 속한 네트워크 주소를 반환하는 함수.
def f_ipv4 (in_ipv4, in_subnet_mask) :
    a = in_ipv4['ipv4_1']&in_subnet_mask['subnet_1']
    b = in_ipv4['ipv4_2']&in_subnet_mask['subnet_2']
    c = in_ipv4['ipv4_3']&in_subnet_mask['subnet_3']
    d = in_ipv4['ipv4_4']&in_subnet_mask['subnet_4']
    
    print('사용자가 속한 네트워크 주소 :',a,'.', b,'.', c,'.', d)



# ipv4, subnet mask 를 입력받아, 사용자가 속한 네트워크 주소의 broad cast 주소를 알려주는 함수.
def broad (in_ipv4, in_subnet_mask) :
    a  = format(in_ipv4['ipv4_1'],'08b')
    b  = format(in_ipv4['ipv4_2'],'08b')
    c  = format(in_ipv4['ipv4_3'],'08b')
    d  = format(in_ipv4['ipv4_4'],'08b')

    e = format(in_subnet_mask['subnet_1'],'08b')
    f = format(in_subnet_mask['subnet_2'],'08b')
    g1 = format(in_subnet_mask['subnet_3'],'08b')
    g2 = format(in_subnet_mask['subnet_4'],'08b')

    h = []
    j = []

    for i in range(len(a)) :
        h.append(a[i])
    for i in range(len(b)) :
        h.append(b[i])
    for i in range(len(c)) :
        h.append(c[i])
    for i in range(len(d)) :
        h.append(d[i])

    for i in range(len(e)) :
        j.append(e[i])
    for i in range(len(f)) :
        j.append(f[i])
    for i in range(len(g1)) :
        j.append(g1[i])
    for i in range(len(g2)) :
        j.append(g2[i])

    k = []
    for i in range(len(j)) :
        if j[i] == '1' :
            k.append(h[i])
        else :
            k.append('1')

    k1 = k[0:8]
    k2 = k[8:16]
    k3 = k[16:24]
    k4 = k[24:32]

    sum1 = f_sum(k1)
    sum2 = f_sum(k2)
    sum3 = f_sum(k3)
    sum4 = f_sum(k4)
    
    print('사용자가 속한 broadcast 주소 : %d . %d . %d . %d'%(sum1, sum2, sum3, sum4))


# 문자열로 한자리씩 띄어서 구성된 이진수를 10진수로 변환
def f_sum (fk) :
    fsum = 0
    for i in range(8) :
        if i == 0 :
            fsum = fsum + (128 * int(fk[i]))
        elif i == 1 :
            fsum = fsum + (64 * int(fk[i]))
        elif i == 2 :
            fsum = fsum + (32 * int(fk[i]))
        elif i == 3 :
            fsum = fsum + (16 * int(fk[i]))
        elif i == 4 :
            fsum = fsum + (8 * int(fk[i]))
        elif i == 5 :
            fsum = fsum + (4 * int(fk[i]))
        elif i == 6 :
            fsum = fsum + (2 * int(fk[i]))
        elif i == 7 :
            fsum = fsum + (1 * int(fk[i]))
    return fsum

# ipv4, subnet mask 를 입력받아, 사용자가 속한 네트워크 주소의 호스트 수를 반환하는 함수. 
def count_host (in_ipv4, in_subnet_mask) :
    a = []

    b = format(in_subnet_mask['subnet_1'],'08b')
    c = format(in_subnet_mask['subnet_2'],'08b')
    d = format(in_subnet_mask['subnet_3'],'08b')
    e = format(in_subnet_mask['subnet_4'],'08b')
    
    for i in range(len(b)) :
        a.append(b[i])
    for i in range(len(c)) :
        a.append(c[i])
    for i in range(len(d)) :
        a.append(d[i])
    for i in range(len(e)) :
        a.append(e[i])
    
    f = a.count('0')
    g = 2 ** f

    print('사용자가 속한 네트워크 주소의 호스트 수 : ', g - 2)


##################################################################################
# https://www.subnet-calculator.com/
# 위의 사이트와 동일한 기능을 수행하는 코드를 작성하는게 이번 프로젝트의 최종목표.
# 사용자 정의 함수를 main 함수에 불러서 사용하는 식으로 코드를 작성.

#main 함수 ->
ipv4 = input_ipv4()
print("")
subnet_mask = input_subnet()
print("")
print('##########################결과출력##########################')
print("")
print("입력된 ip주소 :  ", ipv4)
print("입력된 서브넷 마스크 주소 :  ",subnet_mask)
print("")

print("입력된 ip 주소를 2진수로 변환")
ad_binary(ipv4)
print("")
print("입력된 subnetmask 주소를 2진수로 변환")
ad_binary(subnet_mask)
print("")

ip_class = f_ip_class(ipv4['ipv4_1'])
print("")

f_ipv4(ipv4, subnet_mask)
print("")

count_host(ipv4, subnet_mask)
print("")

broad(ipv4, subnet_mask)

##################################################################################
        



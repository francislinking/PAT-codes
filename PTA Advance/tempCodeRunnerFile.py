import math
def IsPrime(Num):
    for i in range(2,int(math.sqrt(Num))+1):
        if Num % i == 0:
            return 0
    return 1

def reverse_Radix(origin_num,base_num):
    result_num_lsit = []
    if origin_num < base_num:
        return origin_num
    else:
        while True:
            div, mod = divmod(origin_num,base_num)
            # result_num_lsit.insert(0,str(mod))
            result_num_lsit.append(str(mod))
            origin_num = div
            if origin_num < base_num:
                # result_num_lsit.insert(0,str(origin_num))
                result_num_lsit.append(str(origin_num))
                result_num = int(''.join(result_num_lsit))
                return result_num

def ToDecimal(origin_num,base_num):
    result_num = 0
    index = 0
    while True:
        div, mod = divmod(origin_num,10)
        result_num = result_num + mod*base_num**index
        index+=1
        origin_num = div
        if div == 0:
            return result_num


while True:
    Input_Str = input().split(' ')
    if int(Input_Str[0]) < 0:
        break

    origin_num = int(Input_Str[0])
    base_num = int(Input_Str[1])

    reverse_num = reverse_Radix(origin_num,base_num)

    result_num = ToDecimal(reverse_num,base_num)

    if IsPrime(origin_num) & IsPrime(result_num):
        print('YES')
    else:
        print('NO')
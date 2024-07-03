def init_per(pt):
    pt_str = list(pt)
    res = [None] * len(pt_str)
    ip_table = [2, 6, 3, 1, 4, 8, 5, 7]
    for i, j in enumerate(ip_table):
        res[i] = pt_str[j-1]
    return "".join(res)

def rev_per(pt):
    pt_str = list(pt)
    res = [None] * len(pt_str)
    ip_table = [4, 1, 3, 5, 7, 2, 8, 6]
    for i, j in enumerate(ip_table):
        res[i] = pt_str[j-1]
    return "".join(res)

def roundfunc(lis, key):
    epbox = [4, 1, 2, 3, 2, 3, 4, 1]
    samp = [None] * len(lis) * 2
    for i, j in enumerate(epbox):
        samp[i] = lis[j-1]
    res = list( str(int(a) ^ int (b)) for a, b in zip(samp, key))
   
    s0 = [[1, 0, 3, 2],
          [3, 2, 1, 0],
          [0, 2, 1, 3],
          [3, 1, 3, 2]]
   
    s1 = [[0, 1, 2, 3],
          [2, 0, 1, 3],
          [3, 0, 1, 0],
          [2, 1, 0, 3]]
    L = str(bin(s0[int(res[0]+res[3], 2)][int("".join(res[1:3]), 2)])).replace('0b', '')
    if len(L)== 1: L = "0"+L
    R = str(bin(s1[int(res[4]+res[7], 2)][int("".join(res[5:7]), 2)])).replace('0b', '')
    if len(R)== 1: R = "0"+R
    p = list(L + R)
    result = [None] * len(lis)
    p4 = [2, 4, 3, 1]
    for i, j in enumerate(p4):
        result[i] = p[j-1]
    return result

def func(pt, key):
    pt_str = list(pt)
    left = pt_str[:4]
    right = pt_str[4:]
    #print(str(bin(int("".join(left), 2) ^ int("".join(roundfunc(right, key)), 2))).replace('0b', ''))
    temp = str(bin(int("".join(left), 2) ^ int("".join(roundfunc(right, key)), 2))).replace('0b', '')
    if len(temp) < 4: temp = ("0"*(4-len(temp)) + temp)
    L = list(temp)
    return L + right
     
def p10(key):
    key_str = list(key)
    res = [None] * len(key_str)
    p10_table = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    for i, j in enumerate(p10_table):
        res[i] = key_str[j-1]
    return "".join(res)

def p8(key):
    key_str = list(key)
    res = [None] * (len(key_str)-2)
    p8_table = [6, 3, 7, 4, 8, 5, 10, 9]
    for i,j in enumerate(p8_table):
        res[i] = key_str[j-1]
    return "".join(res)

def shift(key, n=0):
    key_str = list(key)
    shifted = "".join(key_str[n+1:]) + "".join(key_str[:n+1])
    return shifted

pt = input("Enter the 8-bit plaintext: ")
inp = init_per(pt)
key = input("Enter the 10-bit key: ")
p10samp = p10(key)
samp = shift(p10samp[:5]) + shift(p10samp[5:])
key1 = p8(samp)
print("Subkey 1 : ", key1)
samp1 = shift(samp[:5], 1) + shift(samp[5:], 1)
key2 = p8(samp1)
print("Subkey 2: ", key2)
temp1 = func(inp, key1)
temp = temp1[4:] + temp1[:4]
temp2 = func(temp, key2)
ct = rev_per(temp2)
print("Plaintext: ", pt, "\nCiphertext: ", ct)
print("Decryption process...")
temp2 = init_per(ct)
temp = func(temp2, key2)
temp1 = temp[4:] + temp[:4]
inp = func(temp1, key1)
revpt = rev_per(inp)
print("Decrypted plaintext: ", revpt)





ls = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36]
rs = [63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]


key = "0000000100100011010001010110011110001001101010111100110111101111"
print('64 bit key:         ',key,'count:',len(key))


pc1 = ""
for element in ls:
    pc1 += key[element]
for e in rs:
    pc1 += key[e]
print('permuted choice 1:  ',pc1,'        count:',len(pc1))

C = ""
D = ""
i = 0
for bit in pc1:
    if i < len(pc1)/2:
        C += pc1[i]
    else:
        D += pc1[i]
    i += 1
print('C: ',C,len(C),'bits')
print('D: ',D,len(D),'bits')

C_lcs =""
D_lcs =""
counter = 1
for bit in C:
    C_lcs += C[counter%len(C)]
    D_lcs += D[counter%len(D)]
    counter += 1
print('C left circular shift:', C_lcs,' \n Bit Length:',len(pc1))
print('D left circular shift:', D_



pc2 = ""

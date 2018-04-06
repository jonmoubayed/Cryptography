ls = [57,49,41,33,25,17,9,
      1,58,50,42,34,26,18,
      10,2,59,51,43,35,27,
      19,11,3,60,52,44,36]
rs = [63,55,47,39,31,23,15,
      7,62,54,46,38,30,22,
      14,6,61,53,45,37,29,
      21,13,5,28,20,12,4]


key = "0000000100100011010001010110011110001001101010111100110111101111"
print('\n64 bit key:         ',key,'count:',len(key))


pc1 = ""
for element in ls:
    pc1 += key[element]
for e in rs:
    pc1 += key[e]
print('permuted choice 1:  ',pc1,'        count:',len(pc1),'\n')


C = ""
D = ""
i = 0
for bit in pc1:
    if i < len(pc1)/2:
        C += pc1[i]
    else:
        D += pc1[i]
    i += 1

#left circular shift
C_lcs = ""
D_lcs = ""
counter = 1
for bit in C:
    C_lcs += C[counter%len(C)]
    D_lcs += D[counter%len(D)]
    counter += 1

    
print('C:',C,len(C),'bits ', end='')
print('D:',D,len(D),'bits') 
print('//////////////////////////////LEFT CURCULAR SHIFT//////////////////////////////')   
print('C:',C_lcs,len(C_lcs),'bits ', end='')
print('D:',D_lcs,len(D_lcs),'bits\n')

CD = C_lcs + D_lcs
pc2 = ""
pc2_table = [14,17,11,24, 1, 5, 3,28,
             15, 6,21,10,23,19,12, 4,
             26, 8,16, 7,27,20,13, 2,
             41,52,31,37,47,55,30,40,
             51,45,33,48,44,49,39,56,
             34,53,46,42,50,36,29,32]
for number in pc2_table:
    pc2 += CD[number-1]
    #print('CD[',number-1,']=',CD[number-1])
print('permuted choice 2:  ',pc2,'                count:',len(pc2),'\n')


ip = ""
ip_table = [58,50,42,34,26,18,10,2,
            60,52,44,36,28,20,12,4,
            62,54,46,38,30,22,14,6,
            64,56,48,40,32,24,16,8,
            57,49,41,33,25,17,9, 1,
            59,51,43,35,27,19,11,3,
            61,53,45,37,29,21,13,5,
            63,55,47,39,31,23,15,7]
for i in ip_table:
    ip += key[i-1]
print('plaintext:          ',key,'count:',len(key))   
print('initial permutation:',ip,'count:',len(ip))


L = ""
R = ""
i = 0
for bit in ip:
    if i < len(ip)/2:
        L += ip[i]
    else:
        R += ip[i]
    i += 1
print('L:',L,len(L),'bits ', end='')
print('R:',R,len(R),'bits') 


E = ""
e_table = [32, 1, 2, 3, 4, 5,
            4, 5, 6, 7, 8, 9,
            8, 9,10,11,12,13,
           12,13,14,15,16,17,
           16,17,18,19,20,21,
           20,21,22,23,24,25,
           24,25,26,27,28,29,
           28,29,30,31,32,1]
for i in e_table:
    E += R[i-1]
print('\n      E[R]:',E,len(E),'bits')


K = pc2
XOR = ""
for i in range(len(E)):
    if E[i] == K[i]:
        XOR += '0'
    else:
        XOR += '1'
print('         K:',K,len(K),'bits')
print('E[R] XOR K:',XOR,len(XOR),'bits')

P = ""
B = "10100101010011101111010010110010"
p_table = [16, 7,20,21,29,12,28,17,
            1,15,23,26, 5,18,31,10,
            2, 8,24,14,32,27, 3, 9,
           19,13,30, 6,22,11, 4,25]
for element in p_table:
    P += B[element-1]
print('\n         B:',B,len(B),'bits')
print('      P(B):',P,len(P),'bits')    
           

R1 = ""
for i in range(len(P)):
    if P[i] == L[i]:
        R1 += '0'
    else:
        R1 += '1'
print('         L:',L,len(L),'bits')
print('P(B) XOR L:',R1,len(R1),'bits')


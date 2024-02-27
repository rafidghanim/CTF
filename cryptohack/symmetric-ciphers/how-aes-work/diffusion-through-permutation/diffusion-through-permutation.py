def shift_rows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]


def inv_shift_rows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[3][1], s[0][1], s[1][1], s[2][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[1][3], s[2][3], s[3][3], s[0][3]
    return s


# learned from http://cs.ucsb.edu/~koc/cs178/projects/JT/aes.c
#xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)
def xtime(a,n=1):
    '''
    Described in 4.2.1 of NIST AES spec.

    Equal to multiplying by one 'x', so perform xtime multiple times to get values other than {02}
    such as {04}
    '''
    for i in range(n):
        if a & 0x80:   # 0x80 is b10000000, so this will be all 0s if highest bit isn't 1
            a = a << 1
            a ^= 0x1B
        else:
            a = a << 1
    return a & 0xFF


def mix_single_column(a):
    # see sec 4.1.2 in The Design of Rijndael
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)


def mix_columns(s):
    for i in range(4):
        mix_single_column(s[i])


#def inv_mix_columns(s):
    # see sec 4.1.3 in The Design of Rijndael
#    for i in range(4):
#        u = xtime(xtime(s[i][0] ^ s[i][2]))
#        v = xtime(xtime(s[i][1] ^ s[i][3]))
#        s[i][0] ^= u
#        s[i][1] ^= v
#        s[i][2] ^= u
#        s[i][3] ^= v

#    inv_shift_rows(s)

def inv_mix_a_column(s):
    '''
    NIST FIPS-197 5.3.3  
    '''
    x = list(s)
    XOR = xtime(s[0],3) ^ xtime(s[1],3) ^ xtime(s[2],3) ^ xtime(s[3],3)
    x[0] = xtime(s[0],2) ^ xtime(s[0]) ^ xtime(s[1]) ^ s[1] ^ xtime(s[2],2) ^ s[2] ^ s[3] ^ XOR
    x[1] = s[0] ^ xtime(s[1],2) ^ xtime(s[1]) ^ xtime(s[2]) ^ s[2] ^ xtime(s[3],2) ^ s[3] ^ XOR
    x[2] = s[1] ^ xtime(s[2],2) ^ xtime(s[2]) ^ xtime(s[3]) ^ s[3] ^ xtime(s[0],2) ^ s[0] ^ XOR
    x[3] = s[2] ^ xtime(s[3],2) ^ xtime(s[3]) ^ xtime(s[0]) ^ s[0] ^ xtime(s[1],2) ^ s[1] ^ XOR
    return x

def inv_mix_columns(s):
    for i in range(4):
        s[i] = inv_mix_a_column(s[i])
    return s

s = [
    [108, 106, 71, 86],
    [96, 62, 38, 72],
    [42, 184, 92, 209],
    [94, 79, 8, 54],
]

fl = (inv_shift_rows(inv_mix_columns(s)))
print(''.join([chr(fl[i][j]) for i in range(len(fl)) for j in range(len(fl))]))

from pwn import xor
#before_s = "151>7;;>:10<1;455761>5;70><<?<=01>?"
s =[1, 5, 1, 14, 7, 11, 11, 14, 10, 1, 0, 12, 1, 11, 4, 5, 5, 7, 6, 1, 14, 5, 11, 7, 0, 14, 12, 12, 15, 12, 13, 0, 1, 14, 15]
v9 = [114, 109, 96, 101, 115, 98, 104, 122, 108, 122, 119, 100, 49, 84, 119, 49, 108, 99, 89, 103, 98, 49, 108, 88, 49, 125, 83, 126, 59, 98, 105, 48, 108, 49, 114]
print(''.join([xor(s[i],v9[i]).decode() for i in range(len(s))]))

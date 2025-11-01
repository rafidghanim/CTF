import math
from Crypto.Util.number import getPrime, bytes_to_long
FLAG = b"REDACTED"
m = bytes_to_long(FLAG)

n = math.prod([getPrime(1024) for _ in range(2**0)])
e = 0x10001
c = pow(m, e, n)

print(f'{n = }\n')
print(f'{e = }\n')
print(f'{c = }\n')

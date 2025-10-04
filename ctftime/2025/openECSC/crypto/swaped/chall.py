from Crypto.Util.number import getPrime

p = getPrime(1024)
q = getPrime(1024)
if p > q:
	p, q = q, p
N = p * q

e = getPrime(500)
d = pow(e, -1, (p-1)*(q-1))
e, d = d, e

primes = [getPrime(256) for _ in range(9)]
e_residues = [e % p for p in primes]

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import sha256

flag = open('flag.txt', 'rb').read()
key = sha256((str(p) + str(q)).encode()).digest()
ct = AES.new(key, AES.MODE_ECB).encrypt(pad(flag, 16)).hex()

open('output.txt', 'w').write(f'''\
{N = }
{primes = }
{e_residues = }
ct = {ct}
''')
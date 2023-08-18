import pwn
import random
import string

def generate_unique_keys(num_keys):
    keys = set()
    while len(keys) < num_keys:
        key_parts = []
        for _ in range(5):
            part = ''.join(random.choices(string.ascii_uppercase, k=4))
            key_parts.append(part)
        key = '-'.join(key_parts)
        if key not in keys:
            keys.add(key)
    return keys

num_keys = 100
keys = generate_unique_keys(num_keys)

# Jika ingin berinteraksi dengan program lokal, uncomment baris berikut
#p = pwn.process('./soal')

# Jika ingin berinteraksi dengan program remote, uncomment baris berikut
p = pwn.remote("34.101.174.85", 10003)

# Hanya salah satu dari dua baris di atas yang harus di-uncomment sesuai kebutuhan

i = 1

for key in keys:
    p.recvuntil(b'==>')
    print(f"{i} => {key}")
    p.sendline(key.encode())
    i += 1

x = p.recvuntil(b'}')
print(f"Flangnya banh:: {x.decode()}")

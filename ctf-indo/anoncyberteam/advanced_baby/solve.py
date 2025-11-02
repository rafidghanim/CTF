from Crypto.Util.number import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

KEY_LEN = 2
BS = 16

iv = bytes.fromhex('3c784c12aaa92edad09c21619d224621')
ct = bytes.fromhex('82c1f7e9196b00932de5408ff82919a9ee263fcae78be1791e93a0a1ff575b5c5acbc74efdaf0e32ba707f614f3e53537bb5a24c0aa83b3e01dd2d7ea75b5d9f47b943a13b56f0fb48b35077e684953e42839c367d1dacc3e585971cdce4778233d77cddb0b33a79b230c85ff30f8dad77936df0de6535335fc51cb3fb78db76')

for i in range(2**8,2**16):
	key = pad(long_to_bytes(i),BS)
	cipher = AES.new(key, AES.MODE_CBC, iv)
	pt = cipher.decrypt(ct)
	print(pt,i)

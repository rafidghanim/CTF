from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('latin-1'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('latin-1')
    else:
        return plaintext.decode('latin-1')

"""
Intercepted from Alice: {"supported": ["DH1536", "DH1024", "DH512", "DH256", "DH128", "DH64"]}
Send to Bob: {"supported": ["DH64"]}
Intercepted from Bob: {"chosen": "DH64"}
Send to Alice: {"chosen": "DH64"}
Intercepted from Alice: {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0xdb11716e63be4dbd"}
Intercepted from Bob: {"B": "0x33cbf414139275ca"}
Intercepted from Alice: {"iv": "83924311f3a8690ee0bf232856fcfba7", "encrypted_flag": "e44ed8ea6c4beb06e5a7d9c0e4c09c21f57ba8b2da9c3ef517202664ec073fc8"}

g^(ab) mod p

for finding a use discrete logarithm
g^a = A mod p
g^b = B mod p
"""


shared_secret = 4263864902655038491
iv = "83924311f3a8690ee0bf232856fcfba7"
ciphertext = "e44ed8ea6c4beb06e5a7d9c0e4c09c21f57ba8b2da9c3ef517202664ec073fc8"

print(decrypt_flag(shared_secret, iv, ciphertext))

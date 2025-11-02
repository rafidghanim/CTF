from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_aes(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = cipher.decrypt(ciphertext)
    decrypted_text = unpad(decrypted_text, AES.block_size)
    return decrypted_text

def main():
    # Ciphertext, key, dan IV yang diberikan
    ciphertext = bytes.fromhex("d213870a02f03a335f6bb7fd410fedb6c26c78d3c173cee31179a281e28840f8d7b046d984d6a180f919338704a926b0667cc41ec24c3cd8a622032b37786ea1")  # Ganti dengan nilai ciphertext yang sebenarnya
    iv = bytes.fromhex("ace4bb8d3d10354ba9cb89422a9bd9e2")  # Ganti dengan nilai IV yang sebenarnya

    # Brute-force untuk nilai kunci AES
    for i in range(256):  # Brute-force untuk byte pertama kunci
        for j in range(256):  # Brute-force untuk byte kedua kunci
            key = bytes([i, j])  # Kombinasikan byte pertama dan kedua untuk membentuk kunci
            decrypted_text = decrypt_aes(ciphertext, key, iv)
            # Tambahkan logika untuk memeriksa apakah hasil dekripsi sudah benar
            # Misalnya, jika hasil dekripsi mengandung kata "FLAG":
            # if b'FLAG' in decrypted_text:
            #     print("Key found!")
            #     print("Decrypted message:", decrypted_text)
            #     break
            # else:
            #     print("Tried key:", key)

if __name__ == "__main__":
    main()

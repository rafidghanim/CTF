def decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        decrypted_text += chr(ord(char) - key)
    return decrypted_text

def main():
    key = 1337
    with open("out.txt", "r") as f:
        ciphertext = f.read().strip()
#    for i in range(0,255):
    plaintext = decrypt(ciphertext, key)
    print("Decrypted message:", plaintext)

if __name__ == "__main__":
    main()

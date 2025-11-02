from secret import FLAG # FIND ME :3

def encrypt(message, key):
    encrypted_text = ""
    for char in message:
        encrypted_text += chr(ord(char) + key)
    return encrypted_text

def main():
    key = 1337
    ciphertext = encrypt(FLAG, key)
    with open("out.txt", "w") as f:
        f.write(ciphertext)

if __name__ == "__main__":
    main()
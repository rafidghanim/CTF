def decrypt(encrypted_text, key):
    decrypted_message = ""
    for char in encrypted_text:
        decrypted_char = chr((ord(char) - key - 32) % 95 + 32)
        decrypted_message += decrypted_char
    return decrypted_message

encrypted_text = "PGSGVHAVFN{g1nc+u4e1+x3A4+R4t1}"
flag = [decrypt(encrypted_text, i) for i in range(0, 255)]
print(flag)

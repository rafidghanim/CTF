def cipher_decrypt(cipher_text, key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_unique = ''.join(sorted(set(key.upper()), key=key.upper().index))
    plain_alphabet = key_unique + ''.join(filter(lambda char: char not in key_unique, alphabet))

    cipher_alphabet = plain_alphabet[::-1]

    decryption_dict = dict(zip(cipher_alphabet, plain_alphabet))

    decrypted_text = ""
    for char in cipher_text.upper():
        if char in decryption_dict:
            decrypted_text += decryption_dict[char]
        else:
            decrypted_text += char

    return decrypted_text

cipher_text = "BKNFUNUCYPIQUGPLICXQKL"
key = "act"
decrypted_message = cipher_decrypt(cipher_text, key)
print("Decrypted message:", f"ACT_CTF{ {decrypted_message.lower()} }")

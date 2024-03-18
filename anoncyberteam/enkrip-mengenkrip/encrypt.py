def cipher_encrypt(plain_text, key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_unique = ''.join(sorted(set(key.upper()), key=key.upper().index))
    plain_alphabet = key_unique + ''.join(filter(lambda char: char not in key_unique, alphabet))

    cipher_alphabet = plain_alphabet[::-1]

    substitution_dict = dict(zip(plain_alphabet, cipher_alphabet))

    encrypted_text = ""
    for char in plain_text.upper():
        if char in substitution_dict:
            encrypted_text += substitution_dict[char]
        else:
            encrypted_text += char

    return encrypted_text

plain_text = "haksorman"
key = "act"
encrypted_message = cipher_encrypt(plain_text, key)
print("Cipher message:", encrypted_message)
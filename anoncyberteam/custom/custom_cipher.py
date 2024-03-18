def custom_cipher(text, shift, alphabet):
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            shifted_index = (alphabet.index(char) + shift) % len(alphabet)
            encrypted_text += alphabet[shifted_index]
        else:
            encrypted_text += char
    return encrypted_text

plaintext = "flag"
list_alphabet = "1234567890ACTQWERYUIOPSDFGHJKLZXVBNM1234567890actqweryuiopsdfghjklzxvbnm"
shift = 17

encrypted_text = custom_cipher(plaintext, shift, list_alphabet)
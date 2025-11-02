def decrypt_custom_cipher(encrypted_text, shift, alphabet):
    decrypted_text = ""
    for char in encrypted_text:
        if char in alphabet:
            shifted_index = (alphabet.index(char) - shift) % len(alphabet)
            decrypted_text += alphabet[shifted_index]
        else:
            decrypted_text += char
    return decrypted_text

# Example usage
encrypted_text = "kmPlHROA38jWIlbHl"
list_alphabet = "1234567890ACTQWERYUIOPSDFGHJKLZXVBNM1234567890actqweryuiopsdfghjklzxvbnm"
shift = 17

decrypted_text = decrypt_custom_cipher(encrypted_text, shift, list_alphabet)
print("Decrypted text:", decrypted_text)

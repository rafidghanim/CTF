def decrypt(crypt, encrypt_alphabet):
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decryption_dict = {encrypt_alphabet[i]: ALPHABET[i] for i in range(len(encrypt_alphabet))}
    
    decrypted_text = ""
    for char in crypt:
        if char in decryption_dict:
            decrypted_text += decryption_dict[char]
        else:
            decrypted_text += char
    
    return decrypted_text

encrypt_alphabet = "ACEGIKMOQSUWYACEGIKMOQSUWY"
crypt = "DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL"

decrypted_text = decrypt(crypt, encrypt_alphabet)
print(decrypted_text)

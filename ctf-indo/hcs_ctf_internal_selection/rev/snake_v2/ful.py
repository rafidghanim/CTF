def decrypt(integrity_check, encrypted_values):
    decrypted_chars = []
    for i in range(len(encrypted_values)):
        # XOR the encrypted value with the corresponding integrity check
        decrypted_char = (encrypted_values[i] ^ integrity_check[i % len(integrity_check)]) & 0xFF
        decrypted_chars.append(chr(decrypted_char))
    return ''.join(decrypted_chars)

def main():
    encrypted_values = [
        0x8c, 0x84, 0xb4, 0x94, 0xc8, 0xaa, 0xb3, 0x8b, 0xa3,
        0xff, 0xa3, 0xb1, 0xab, 0xbf, 0xb4, 0xd0, 0xe6, 0x93,
        0xea, 0xce
    ]
    
    # Coba nilai player_score dari 0 sampai 999999
    for player_score in range(1000000):
        # Hitung jumlah makanan yang dimakan
        times_food_eaten = player_score // 1  # Misalkan speed_size = 1
        integrity_check = times_food_eaten * 0x539
        
        # Buat list dari angka untuk integrity_check
        integrity_check_values = [integrity_check & 0xFF] * len(encrypted_values)
        
        # Dekripsi
        decrypted_message = decrypt(integrity_check_values, encrypted_values)
        
        # Cek apakah pesan terdekripsi mengandung "hcs" atau "HCS"
        if "hcs" in decrypted_message.lower():
            print(f"Integrity Check: {integrity_check}, Player Score: {player_score}, Decrypted Message: {decrypted_message}")
            break

if __name__ == "__main__":
    main()

from cryptography.fernet import Fernet

def load_key(filename):
    with open(filename, 'rb') as f:
        return f.read()

def decrypt_image(encrypted_image_path, key):
    with open(encrypted_image_path, 'rb') as f:
        encrypted_data = f.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    with open('decrypted_image.jpg', 'wb') as f:
        f.write(decrypted_data)

# Load the key from the file
key = load_key('encryption_key.key')

# Decrypt the image
decrypt_image('gambar_encrypted.jpg', key)

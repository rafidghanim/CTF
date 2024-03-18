from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename):
    with open(filename, 'wb') as f:
        f.write(key)

def encrypt_image(image_path, key):
    with open(image_path, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open('gambar_encrypted.jpg', 'wb') as f:
        f.write(encrypted_data)

key = generate_key()

save_key(key, 'encryption_key.key')

encrypt_image('image.jpg', key)

def decrypt(ciphertext):
    possible_flags = []

    for i in range(len(ciphertext)):
        decrypted_byte_found = False
        for possible_key in range(256):
            a = (ciphertext[i] >> 8) & 0xFF
            b = ciphertext[i] & 0xFF
            x_candidate = (a | b)
            if (x_candidate & possible_key == a) and (x_candidate & ~possible_key == b):
                decrypted_byte_found = True
                possible_flags.append(x_candidate)
                break
        if not decrypted_byte_found:
            print(f"Unable to decrypt byte {i}")
            return None

    return bytes(possible_flags)

with open('output.txt', 'r') as file:
    content = file.read()

start_index = content.find('[')
end_index = content.find(']') + 1
ciphertext_str = content[start_index:end_index]
import ast
ciphertext_list = ast.literal_eval(ciphertext_str)
print(decrypt(ciphertext_list))

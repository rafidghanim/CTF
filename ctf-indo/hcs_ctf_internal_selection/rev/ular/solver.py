import itertools

def hex_target():
    return 'd7d63743f5e60386479707f5a733f593e63346e633775793b7353484'

def password_to_hex(password):
    return password.encode().hex()

def find_correct_password(target_hex):
    # Define the prefix and suffix
    prefix = 'HCS{'
    suffix = '}'
    charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    # Calculate the number of characters in the prefix and suffix
    prefix_length = len(prefix)
    suffix_length = len(suffix)

    # Calculate the length for the middle part
    total_length = len(target_hex) // 2
    middle_length = total_length - prefix_length - suffix_length

    # Ensure middle length is non-negative
    if middle_length < 0:
        print("No valid password length.")
        return None

    for middle_tuple in itertools.product(charset, repeat=middle_length):
        middle_part = ''.join(middle_tuple)
        password = f"{prefix}{middle_part}{suffix}"
        
        if password_to_hex(password)[-len(target_hex):] == target_hex:
            return password

    return None

if __name__ == '__main__':
    target_hex_value = hex_target()
    result = find_correct_password(target_hex_value)
    
    if result:
        print(f'Found password: {result}')
    else:
        print('No matching password found.')

def check_password(a):
    # Get user input and encode it
    password = a.encode()
    
    # Check if the encoded password's hex representation matches the target
    if password.hex()[:42] == 'd7d63743f5e60386479707f5a733f593e63346e633775793b7353484':
        print("medeni rek!")
    else:
        print("maaf anda kurang beruntung")
a = input()
check_password(a)

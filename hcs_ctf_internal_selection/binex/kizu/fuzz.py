from pwn import *
import random
import string

# Target binary
exe = './main'  # Replace with the path to your compiled binary

# Function to generate random inputs for fuzzing
def generate_input():
    length = random.randint(1, 2)  # The vulnerable code limits the input to 2 characters
    fuzz_input = ''.join(random.choice(string.ascii_letters + string.digits + '%p%p%') for _ in range(length))
    return fuzz_input

# Setup the process (you can use remote for networked services)
def start():
    return process(exe)

# Fuzzing loop
def fuzz():
    for i in range(100):  # Set a loop for the number of fuzzing attempts
        p = start()
        try:
            # Get the prompt from the binary
            p.recvuntil(b"i'll repeaat anything u say, try it: ")

            # Generate a fuzzing input
            fuzz_input = generate_input()
            print(f"[{i+1}] Sending input: {fuzz_input}")

            # Send the input
            p.sendline(fuzz_input)

            # Capture the response
            response = p.recvall(timeout=1)
            print(f"    Received: {response.decode(errors='ignore')}")

        except EOFError:
            print(f"    Process crashed!")
        finally:
            p.close()

if __name__ == "__main__":
    fuzz()

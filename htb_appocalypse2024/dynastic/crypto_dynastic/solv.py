from pwn import *

# Set up the connection
host = '94.237.60.39'
port = 42145

# Connect to the server
conn = remote(host, port)

# Receive the initial message
print(conn.recvuntil(b'(y/n)'))

# Send 'y' to indicate readiness
conn.sendline(b'y')

# Receive the game start message
print(conn.recvline())

# Game loop
while True:
    # Receive the scenario
    scenario = conn.recvline().strip()

    # Print the scenario
    print("Scenario:", scenario.decode())

    # Parse the scenario and determine the response
    response = []
    if b'GORGE' in scenario:
        response.append(b'STOP')
    if b'PHREAK' in scenario:
        response.append(b'DROP')
    if b'FIRE' in scenario:
        response.append(b'ROLL')

    # Send the response
    conn.sendline(b'-'.join(response))

    # Receive and print the result
    print(conn.recvline().strip())

# Close the connection
conn.close()

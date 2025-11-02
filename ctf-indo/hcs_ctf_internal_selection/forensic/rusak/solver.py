def swap_bytes(data):
    swapped_data = bytearray()
    for i in range(0, len(data), 2):
        chunk = data[i:i+2]
        if len(chunk) == 2:
            swapped_chunk = chunk[1:2] + chunk[0:1]
        else:
            swapped_chunk = chunk
        swapped_data.extend(swapped_chunk)
    return swapped_data

with open('broken_flag', 'rb') as file:
    gambar_bytes = file.read()

swapped_bytes = swap_bytes(gambar_bytes)

with open('swapped_gambar.png', 'wb') as file:
    file.write(swapped_bytes)

print("Proses pertukaran setiap dua byte selesai!")

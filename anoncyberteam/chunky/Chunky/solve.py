from PIL import Image

def reconstruct_image(chunks, num_chunks):
    chunk_width, chunk_height = chunks[0].size

    original_width = chunk_width * num_chunks
    original_height = chunk_height * num_chunks

    result_image = Image.new('RGB', (original_width, original_height))

    for i in range(num_chunks):
        for j in range(num_chunks):
            index = i * num_chunks + j
            result_image.paste(chunks[index], (i * chunk_width, j * chunk_height))

    return result_image.resize((2000, 500))

image_path = "image.jpg"
num_chunks = 5
chunks = [Image.open(f"chunk_{i}.jpg") for i in range(num_chunks*num_chunks)]

original_image = reconstruct_image(chunks, num_chunks)
original_image.show()
original_image.save("original_image.jpg")

from PIL import Image

def create_chunks(image_path, num_chunks):

    image = Image.open(image_path)
    width, height = image.size

    chunk_width = width // num_chunks
    chunk_height = height // num_chunks

    chunks = []

    for i in range(num_chunks):
        for j in range(num_chunks):
            x1 = i * chunk_width
            y1 = j * chunk_height
            x2 = x1 + chunk_width
            y2 = y1 + chunk_height
            chunk = image.crop((x1, y1, x2, y2))
            chunks.append(chunk)

    return chunks

image_path = "image.jpg"
num_chunks = 5
chunks = create_chunks(image_path, num_chunks)

for i, chunk in enumerate(chunks):
    chunk.show()
    chunk.save(f"chunk_{i}.jpg")

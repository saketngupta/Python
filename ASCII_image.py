from PIL import Image

chars = "@%#*+=-:. "

image = Image.open(
    input("Image path: ")
).convert("L")

width = 80
height = int(
    image.height / image.width * width * 0.5
)

image = image.resize((width, height))

pixels = list(image.getdata())

for y in range(height):
    line = ""

    for x in range(width):
        pixel = pixels[y * width + x]

        index = pixel * (len(chars) - 1) // 255

        line += chars[index]

    print(line)
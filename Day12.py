from PIL import Image
import random


INPUT_IMAGE = "Image.jpg"
OUTPUT_IMAGE = "output.jpg"

# Number of horizontal strips
NUMBER_OF_STRIPS = 12



img = Image.open(INPUT_IMAGE).convert("RGB")

width, height = img.size

# Create output image
output = Image.new("RGB", (width, height), "black")

# Calculate strip height
strip_height = height // NUMBER_OF_STRIPS

strips = []

#horizontally crop the image into strips

for i in range(NUMBER_OF_STRIPS):

    top = i * strip_height

    if i == NUMBER_OF_STRIPS - 1:
        bottom = height
    else:
        bottom = (i + 1) * strip_height

    # Crop horizontal strip
    strip = img.crop((0, top, width, bottom))

    strips.append(strip)




random.shuffle(strips)


# PASTE STRIPS VERTICALLY

current_y = 0

for strip in strips:

    output.paste(strip, (0, current_y))

    current_y += strip.height




output.save(OUTPUT_IMAGE, quality=95)

print("Done!")
print(f"Saved as: {OUTPUT_IMAGE}")
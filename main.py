from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageDraw, ImageFont
import random

# Open the image file
image = Image.open("example.jpg")

# Resize the image
image = image.resize((800, 600))

# Apply a filter to the image
image = image.filter(ImageFilter.GaussianBlur(radius=10))

# Flip the image horizontally
image = ImageOps.mirror(image)

# Convert the image to grayscale
image = ImageOps.grayscale(image)

# Apply a color tint to the image
r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
color_mask = Image.new("RGB", image.size, (r, g, b))
image = Image.blend(image, color_mask, alpha=0.5)

# Adjust the brightness and contrast of the image
enhancer = ImageEnhance.Brightness(image)
image = enhancer.enhance(1.5)

enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(1.5)

# Add text to the image
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", size=50)
text = "Hello, world!"
text_width, text_height = draw.textsize(text, font=font)
x = (image.width - text_width) / 2
y = (image.height - text_height) / 2
draw.text((x, y), text, font=font, fill=(255, 255, 255))

# Save the edited image
image.save("edited_example.jpg")

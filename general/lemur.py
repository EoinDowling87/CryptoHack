from PIL import Image, ImageChops

# Open images
im1 = Image.open("flag.png").convert("1")
im2 = Image.open("lemur.png").convert("1")

result = ImageChops.logical_xor(im1,im2)
result.save("result.png")
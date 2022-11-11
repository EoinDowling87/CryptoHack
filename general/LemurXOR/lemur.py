from PIL import Image, ImageChops
picture1 = Image.open("/home/b00123313/Desktop/CryptoHack/general/LemurXOR/lemar.png")
picture2 = Image.open("/home/b00123313/Desktop/CryptoHack/general/LemurXOR/flag.png")
picture3 = ImageChops.add(ImageChops.subtract(picture2, picture1), ImageChops.subtract(picture1, picture2))
picture3.show()
picture3.save("/home/b00123313/Desktop/CryptoHack/general/LemurXOR/picture3.png")
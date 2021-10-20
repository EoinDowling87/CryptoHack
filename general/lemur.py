from PIL import Image, ImageChops
pic1 = Image.open("/home/b00123313/Desktop/CryptoHack/general/LemurXOR/lemar.png")
pic2 = Image.open("/home/b00123313/Desktop/CryptoHack/general/LemurXOR/flag.png")
pic3 = ImageChops.add(ImageChops.subtract(pic2, pic1), ImageChops.subtract(pic1, pic2))
pic3.show()
pic3.save("/home/b00123313/Desktop/CryptoHack/general/LemurXOR//lemrpic3.png")
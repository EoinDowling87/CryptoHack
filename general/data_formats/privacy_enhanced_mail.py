from Crypto.PublicKey import RSA


rsa_key = RSA.import_key(open('/home/b00123313/Desktop/CryptoHack/general/data_formats/transparency.pem', 'rb').read())

print(rsa_key.n)

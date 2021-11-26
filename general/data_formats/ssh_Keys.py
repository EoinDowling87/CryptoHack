from Crypto.PublicKey import RSA


rsa_key = RSA.import_key(open('/home/b00123313/Desktop/CryptoHack/general/data_formats/bruce_rsa.pub', 'rb').read())

print(rsa_key.n)
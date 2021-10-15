
big_integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

hex_data = hex(big_integer)

byte_data = bytes.fromhex(hex_data[2:])
print(byte_data.decode("utf-8"))